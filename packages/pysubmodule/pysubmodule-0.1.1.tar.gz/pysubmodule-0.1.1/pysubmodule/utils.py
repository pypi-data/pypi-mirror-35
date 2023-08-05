import json
import os
from .logger import logger
from .git_operator import *


GIT_FUNC_DICT = {
    'clone': git_clone,
    'update': git_pull,
    'version': git_version,
}


def load_json(json_config_path):
    if not os.path.exists(json_config_path):
        raise FileNotFoundError('json file not found in {}'.format(json_config_path))
    with open(json_config_path) as json_config_file:
        raw_res_dict = json.load(json_config_file)
    root_path = os.path.dirname(json_config_path)

    new_res_dict = dict()
    for res_name, res_value in raw_res_dict.items():
        git_url = res_value['url']
        dst_path = res_value['path']
        desc = res_value['desc']
        real_res_name = git_url.split('/')[-1].split('.')[0]
        if dst_path == '.':
            dst_abs_path = root_path
        else:
            dst_abs_path = os.path.join(root_path, dst_path)
        dst_dir_abs_path = os.path.join(dst_abs_path, real_res_name)
        new_item = {
            'url': git_url,
            'path': dst_abs_path,
            'desc': desc,
            'real_name': real_res_name,
        }
        if os.path.exists(dst_dir_abs_path):
            new_item['action'] = 'update'
        else:
            new_item['action'] = 'clone'
        new_res_dict[res_name] = new_item

    return new_res_dict


def apply_action(res_dict):
    for each_res_name, each_res in res_dict.items():
        logger.msg('SYNC', name=each_res_name, **each_res)
        action_name = each_res['action']
        GIT_FUNC_DICT[action_name](each_res)
