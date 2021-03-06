#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import cfg
import helper

def main():
    if not os.path.exists("restart.py"):
        return "restart.py not exist"
    
    crontab_tmp = "./crontab_tmp"
    helper.crontab_to_file(crontab_tmp)
    
    try:
        line_numbers = helper.grep_line_numbers(cfg.timer_commamd(), crontab_tmp)
        if len(line_numbers) != 0:
            return "timer already installed"

        # 添加定时重启命令
        helper.append_file(cfg.timer_commamd(), crontab_tmp)

        # 将定时脚本加载到crontab
        if helper.crontab_load_file(crontab_tmp):
            return "timer install success"
        else:
            return "timer install failed"
    finally:
        helper.remove_file(crontab_tmp)




if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    print main()