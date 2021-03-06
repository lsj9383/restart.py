#!/usr/bin/python
# -*- coding:utf-8 -*-

import helper
import os
import cfg

def main():
    # 根据程序名称获取pid
    pid = helper.get_pid(cfg)

    # 若pid不存在，则进程已经停止
    if not pid:
        helper.remove_file(cfg.pid_lock())
        return "{0} not run".format(cfg.name())

    # 关闭进程
    helper.stop_proc(pid)

    # 若pid不存在，则进程停止成功
    if not helper.get_pid(cfg):
        helper.remove_file(cfg.pid_lock())
        return "{0}({1}) stop success".format(cfg.name(), pid)
    else:
        return "{0}({1}) stop failed".format(cfg.name(), pid)

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    print main()
