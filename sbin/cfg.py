# -*- coding:utf-8 -*-

process_path = "../server/runserver.py"
process_cmd  = "nohup {0} > /dev/null 2>&1 &"
search_pid_type = 0

def init():
    import os
    global process_path
    global process_name
    global process_cmd
    os.chdir(os.path.dirname(__file__))
    
    process_name = os.path.basename(process_path)
    process_path = os.path.abspath(process_path)
    process_cmd  = process_cmd.format(process_path)

init()