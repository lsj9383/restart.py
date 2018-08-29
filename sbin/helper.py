# -*- coding:utf-8 -*-

import os

os.chdir(os.path.dirname(__file__))

def get_pid(cfg):
    find_pids_cmd = "ps aux|grep {0}|xargs".format(cfg.process_name)
    lines = os.popen(find_pids_cmd).readlines()
    for line in lines:
        pid = line.split(" ")[1]
        print pid
        pfd = os.popen("readlink /proc/{0}".format(pid))
        pid_path = pfd.readline().strip()
        print pid_path
        if pid_path == cfg.process_path:
            return pid
    return None

def start_proc(cfg):
    os.system(cfg.process_cmd)

def stop_proc(cfg):
    pass