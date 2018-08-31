#!/usr/bin/python
# -*- coding:utf-8 -*-

import helper
import os
import cfg

def main():
    # 文件不存在，则无法重启
    if not os.path.exists(cfg.process_path):
        return "{0} not exist".format(cfg.process_name)

    # pid锁文件不存在，则不进行重启
    if not os.path.exists(cfg.process_pid):
        return "{0}.pid not exist, give up restart".format(cfg.process_name)

    # 获取进程pid文件
    pid = helper.get_pid(cfg)
    if pid:
        os.system("echo {0} > {1}.pid".format(pid, cfg.process_path))
        return "{0}({1}) is running".format(cfg.process_name, pid)
    
    # 启动
    helper.start_proc(cfg)

    # 检查是否重启成功
    pid = helper.get_pid(cfg)
    if pid:
        os.popen("echo {0} > {1}.pid".format(pid, cfg.process_path))
        return "{0}({1}) restart success".format(cfg.process_name, pid)
    else:
        return "{0} restart failed".format(cfg.process_name)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    msg = main()
    if msg:
        print msg