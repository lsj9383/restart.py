#!/usr/bin/python
# -*- coding:utf-8 -*-

import helper
import os
import cfg

def main():
    # 文件不存在，则无法重启
    if not os.path.exists(cfg.path()):
        return "{0} not exist".format(cfg.name())

    # pid锁文件不存在，则不进行重启
    if not os.path.exists(cfg.pid_lock()):
        return "{0}.pid not exist, give up restart".format(cfg.name())

    # 获取进程pid文件
    pid = helper.get_pid(cfg)
    if pid:
        helper.cover_file(pid, cfg.pid_lock())
        return "{0}({1}) is running".format(cfg.name(), pid)
    
    # 启动
    helper.start_proc(cfg)

    # 检查是否重启成功
    pid = helper.get_pid(cfg)
    if pid:
        helper.cover_file(pid, cfg.pid_lock())
        return "{0}({1}) restart success".format(cfg.name(), pid)
    else:
        return "{0} restart failed".format(cfg.name())


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    print main()