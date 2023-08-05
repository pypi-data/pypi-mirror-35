import subprocess
import os
from contextlib import contextmanager
from .logger import logger


GIT_CMD_DICT = {
    'clone': ('git', 'clone'),
    'update': ('git', 'pull', '--rebase'),
    'version': ('git', '--version'),
}


@contextmanager
def workspace_manager(new_workspace):
    old_workspace = os.getcwd()
    os.chdir(new_workspace)
    yield
    os.chdir(old_workspace)


def run_cmd(cmd):
    return_code = subprocess.call(cmd)
    if return_code:
        raise RuntimeError(cmd)
    return True


def git_clone(res_dict):
    res_url = res_dict['url']
    dst_path = res_dict['path']
    os.makedirs(dst_path, exist_ok=True)
    with workspace_manager(dst_path):
        git_pull_cmd = list(GIT_CMD_DICT['clone']) + [res_url]
        git_pull_cmd_str = ' '.join(git_pull_cmd)
        logger.msg('GIT CLONE', cmd=git_pull_cmd_str, cur_directory=dst_path)
        run_cmd(git_pull_cmd)


def git_pull(res_dict):
    real_name = res_dict['real_name']
    dst_path = res_dict['path']
    dst_workspace = os.path.join(dst_path, real_name)
    with workspace_manager(dst_workspace):
        git_pull_cmd = ['git', 'pull', '--rebase']
        git_pull_cmd_str = ' '.join(git_pull_cmd)
        logger.msg('GIT PULL', cmd=git_pull_cmd_str, cur_directory=dst_workspace)
        run_cmd(git_pull_cmd)


def git_version():
    run_cmd(['git', '--version'])


__all__ = [
    'git_clone',
    'git_version',
    'git_pull',
]
