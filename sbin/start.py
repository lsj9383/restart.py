#!/usr/bin/python
# -*- coding:utf-8 -*-

import helper
import os
import cfg

def main():
    # 判断进程文件是否存在
    if not os.path.exists(cfg.path()):
        return "process file '{0}' not exist".format(process_path)

    # 根据程序名称获取pid, 若pid存在，则进程已经运行，刷新pid锁文件
    pid = helper.get_pid(cfg)
    if pid:
        helper.cover_file(pid, cfg.pid_lock())
        return "{0}({1}) is running".format(cfg.name(), pid)

    # 启动进程
    helper.start_proc(cfg)

    # 根据查询名称查询pid，若成功，则进程已经启动，否则进程启动失败
    pid = helper.get_pid(cfg)
    if pid:
        helper.cover_file(pid, cfg.pid_lock())
        return "{0}({1}) start success".format(cfg.name(), pid)
    else:
        return "{0} start failed".format(cfg.name())

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    print main()
