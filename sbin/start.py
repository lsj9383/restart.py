# -*- coding:utf-8 -*-

import helper
import os
import cfg

def main():
    process_path = cfg.process_path
    if not os.path.exists(process_path):
        return "process file '{0}' not exist.".format(process_path)
    pid = helper.get_pid(cfg)
    if pid:
        return "the process(pid={0}) is running.".format(pid)
    # helper.start_proc()
    return "{0} start success".format(cfg.process_name)

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    print main()