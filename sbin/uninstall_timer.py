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
        if len(line_numbers) == 0:
            return "timer not install"
        else:
            for number in line_numbers:
                helper.remove_file_line(number, crontab_tmp)
            helper.crontab_load_file(crontab_tmp)
            return "timer remove success"
    finally:
        helper.remove_file(crontab_tmp)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    print main()