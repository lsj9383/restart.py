# -*- coding:utf-8 -*-

import os

class SearchDirType:
    lsof_cwd = 0
    proc_cwd = 1
    proc_exe = 2
    

__fpath__ = "../server/runserver.py"
__interpreter__ = os.popen("which python").read().strip()
__startup__ = "nohup {__interpreter__} {__fpath__} > /dev/null 2>&1 &"
__search_dir_type__ = SearchDirType.lsof_cwd

# init

os.chdir(os.path.dirname(__file__))
__fname__ = os.path.basename(__fpath__)
__fpath__ = os.path.abspath(__fpath__)
__startup__  = __startup__.format(__interpreter__=__interpreter__, __fpath__ = __fpath__)
__pid_lock__ = __fpath__+".pid"
__timer_comment__ = "\n### {0} restart command".format(__fname__)
__timer_command__ = "* * * * * cd {0} && {1} ./restart.py > /dev/null 2>&1".format(
                        os.getcwd(), __interpreter__)

# interface
def name():
    return __fname__

def path():
    return __fpath__

def startup():
    return __startup__

def pid_lock():
    return __pid_lock__

def search_dir_type():
    return __search_dir_type__

def timer_comment():
    return __timer_comment__

def timer_commamd():
    return __timer_command__

def interpreter():
    return __interpreter__