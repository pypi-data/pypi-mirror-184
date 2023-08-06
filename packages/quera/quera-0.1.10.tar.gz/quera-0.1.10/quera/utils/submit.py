import importlib
import json
import os
import urllib.parse
import zipfile
from getpass import getpass
from pathlib import Path
from typing import Optional

import requests
import xattr
from quera.utils.cache import cache, cached

JUDGE_API = 'https://mirror.quera.org/judge_api/apikey-judge/'
CONFIG_NAME = '.quera_config'


@cached
def __get_current_file_id():
    try:
        response = requests.get('http://172.28.0.2:9000/api/sessions').json()
    except requests.exceptions.JSONDecodeError:
        print('Colab Error: please call quera support; colab api session is not working.')
        return None
    if len(response) > 0 and 'path' in response[0] and 'fileId=' in response[0]['path']:
        _file_id = response[0]['path'].split('=', 1)[1]
        return urllib.parse.unquote(_file_id)

    return None


def get_file_id(path):
    try:
        return xattr.getxattr(path, 'user.drive.id').decode()
    except (OSError, FileNotFoundError):
        return None


@cached
def get_colab_current_file_path() -> Optional[Path]:
    try:
        drive = importlib.import_module('.drive', 'google.colab')
    except ModuleNotFoundError:
        return None

    drive_path = '/content/drive'
    drive.mount(drive_path)

    file_id = __get_current_file_id()
    if file_id is None:
        return None

    for dir_path, _, files in os.walk(f'{drive_path}/MyDrive/Quera/'):
        file_path = next(
            filter(
                lambda x: file_id == get_file_id(x),
                filter(
                    lambda x: x.endswith('.ipynb'),
                    map(
                        lambda x: os.path.join(dir_path, x),
                        files
                    )
                )
            ),
            None
        )
        if file_path is not None:
            return Path(file_path)

    return None


@cached
def get_quera_config():
    current_file = get_colab_current_file_path()
    if current_file is not None:
        sibling_files = current_file.parent.iterdir()
        config_file = next(filter(lambda f: f.is_file and f.name == CONFIG_NAME, sibling_files), None)
        if config_file is not None:
            return json.loads(config_file.read_text())

    return None


def get_config_attr(key):
    config = get_quera_config()
    if config is not None:
        return config.get(key, None)

    return None


def get_apikey() -> str:
    if 'apikey' not in cache:
        apikey = get_config_attr('apikey')
        if apikey is not None:
            return apikey

        print('Enter you APIKey please:')
        cache['apikey'] = getpass('Quera APIKey: ')

    return cache['apikey']


def get_problem_id() -> int:
    if 'problem_id' not in cache:
        problem_id = get_config_attr('problem_id')
        if problem_id is None:
            raise Exception('problem_id not found')

    return cache['problem_id']


def get_file_type_id() -> int:
    if 'file_type_id' not in cache:
        file_type_id = get_config_attr('file_type_id')
        if file_type_id is None:
            raise Exception('file_type_id not found')

    return cache['file_type_id']


def submit(*, submitting_file_name: str = 'result.zip', api: str = JUDGE_API):
    problem_id = get_problem_id()
    file_type_id = get_file_type_id()

    with open(submitting_file_name, 'rb') as result:
        response = requests.post(
            api,
            files={'file': result},
            data={'problem_id': problem_id, 'file_type': file_type_id},
            headers={'Judge-APIKey': get_apikey()}
        )
        if response.status_code != 201:
            print(f'Error - {response.status_code}: ', response.content.decode())
        else:
            print('Submitted to Quera Successfully')


def submit_files(file_names: list = None):
    if not file_names:
        raise Exception('No files selected to submit')

    with zipfile.ZipFile("result.zip", mode="w") as zf:
        for file_name in file_names:
            zf.write('./' + file_name, file_name, compress_type=zipfile.ZIP_DEFLATED)

    submit(submitting_file_name="result.zip")
