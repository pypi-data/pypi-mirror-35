import base64
import json
import yaml
import os

from os.path import join

from common.constants import CONFIG_FILE_PATH
COMMON_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def decode_base64_string(encoded_data):
    return str(base64.b64decode(encoded_data), 'utf-8')


def decode_base64_json(encoded_data):
    return json.loads(str(base64.b64decode(encoded_data), 'utf-8'))


def get_config(key, attribute):
    """
    :param key: specify vra or xstream as mentioned in the yaml file
    :param attribute: specify the parameter who's value is to be determined
    :return: value corresponding to the parameter
    """
    param_value = None
    with open(join(COMMON_BASE_DIR, CONFIG_FILE_PATH), 'r') as f:
        doc = yaml.load(f)
    if doc and key in doc:
        param_value = doc[key][attribute]
    return param_value
