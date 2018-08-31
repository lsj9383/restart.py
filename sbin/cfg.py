# -*- coding:utf-8 -*-

class SearchPidType:
    lsof_cwd = 0
    proc_cwd = 1
    proc_exe = 2
    

__fpath__ = "../server/runserver.py"
__startup__ = "nohup {__fpath__} > /dev/null 2>&1 &"
__search_dir_type__ = SearchPidType.lsof_cwd

# init
import os

__fname__ = os.path.basename(__fpath__)
__fpath__ = os.path.abspath(__fpath__)
__startup__  = __startup__.format(__fpath__ = __fpath__)
__pid_lock__ = __fpath__+".pid"

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