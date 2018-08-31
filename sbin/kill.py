#!/usr/bin/python
# -*- coding:utf-8 -*-

import helper
import os
import cfg

def main():
    # 若pid不存在，则进程已经停止
    pid = helper.get_pid(cfg)
    if not pid:
        return "{0} not run".format(cfg.name())

    # 杀死进程
    helper.kill_proc(pid)

    if not helper.get_pid(cfg):
        return "{0}({1}) kill success".format(cfg.name(), pid)
    else:
        return "{0}({1}) kill failed".format(cfg.name(), pid)

if __name__ == "__main__":
    print main()