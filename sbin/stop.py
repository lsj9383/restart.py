#!/usr/bin/python
# -*- coding:utf-8 -*-

import helper
import os
import cfg

def remove_file(file):
    try:
        os.remove(file)
    finally:
        return None

def main():
    # 根据程序名称获取pid
    pid = helper.get_pid(cfg)

    # 若pid不存在，则进程已经停止
    if not pid:
        remove_file(cfg.process_pid)
        return "{0} not run".format(cfg.process_name)

    # 关闭进程
    helper.stop_proc(pid)

    # 若pid不存在，则进程停止成功
    if not helper.get_pid(cfg):
        remove_file(cfg.process_pid)
        return "{0}({1}) stop success".format(cfg.process_name, pid)
    else:
        return "{0}({1}) stop failed".format(cfg.process_name, pid)

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    print main()
