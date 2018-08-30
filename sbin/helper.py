# -*- coding:utf-8 -*-

import os

os.chdir(os.path.dirname(__file__))

def pid2cwd(pid):
    pfd = os.popen("readlink /proc/{0}/cwd".format(pid))
    return pfd.readline().strip()

def get_pid(cfg):
    find_pids_cmd = "ps aux|grep {0}|awk '{{print $2;}}'".format(cfg.process_name)
    pids = os.popen(find_pids_cmd).readlines()
    for pid in pids:
        pid = int(pid.strip())
        pid_cwd = pid2cwd(pid)
        if len(pid_cwd) == 0:
            continue
        pid_path = os.path.abspath(pid_cwd+"/"+cfg.process_name)
        if pid_path == cfg.process_path:
            return pid
    return None

def start_proc(cfg):
    os.chdir(os.path.dirname(cfg.process_path))
    os.system(cfg.process_cmd)
    os.chdir(os.path.dirname(__file__))

def stop_proc(pid):
    os.kill(int(pid), 15)