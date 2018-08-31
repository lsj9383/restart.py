# -*- coding:utf-8 -*-

import os

os.chdir(os.path.dirname(__file__))

def dir_from_proc_cwd(pid):
    pfd = os.popen("readlink /proc/{0}/cwd".format(pid))
    return pfd.readline().strip()

def dir_from_lsof_cwd(pid):
    pfd = os.popen("lsof -p {0}|grep cwd|awk '{{print $9;}}'".format(pid))
    return pfd.readline().strip()

def dir_from_proc_exe(pid):
    pfd = os.popen("readlink /proc/{0}/exe".format(pid))
    return os.path.dirname(pfd.readline().strip())

def get_pid(cfg):
    # 入口程序目录获取方案映射
    dir_method_mapper = {
        cfg.SearchPidType.lsof_cwd : dir_from_lsof_cwd,
        cfg.SearchPidType.proc_cwd : dir_from_proc_cwd,
        cfg.SearchPidType.proc_exe : dir_from_proc_exe,
    }
    # 查询可能的pid
    find_pids_cmd = "ps aux|grep {0}|awk '{{print $2;}}'".format(cfg.name())
    pids = os.popen(find_pids_cmd).readlines()

    # 检查pid是否为程序的pid
    for pid in pids:
        pid = int(pid.strip())
        # 获取pid所对应的程序的目录，获取目录默认采用lsof命令方案
        dir_method = dir_method_mapper.get(cfg.search_dir_type(), dir_from_lsof_cwd)
        dir_from_pid = dir_method(pid)
        # 程序目录和程序名称组合成程序路径，查看是否匹配
        path_from_pid = os.path.abspath(dir_from_pid+"/"+cfg.name())
        if path_from_pid == cfg.path():
            return pid
    return None

def start_proc(cfg):
    os.chdir(os.path.dirname(cfg.path()))
    os.system(cfg.startup())
    os.chdir(os.path.dirname(__file__))

def stop_proc(pid):
    os.kill(int(pid), 15)

def kill_proc(pid):
    os.kill(int(pid), 9)