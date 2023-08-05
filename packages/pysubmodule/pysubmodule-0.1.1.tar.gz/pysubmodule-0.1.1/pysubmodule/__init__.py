import pprint
import pysubmodule.utils


def sync(json_config_path):
    utils.git_version()
    git_res_dict = utils.load_json(json_config_path)
    pprint.pprint(git_res_dict)
    utils.apply_action(git_res_dict)
