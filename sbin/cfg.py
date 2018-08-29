# -*- coding:utf-8 -*-

process_path = "../server/runserver.py"
process_cmd  = "nohup python {0} &".format(process_path)

def init():
    import os
    global process_path
    global process_name
    os.chdir(os.path.dirname(__file__))
    
    process_name = os.path.basename(process_path)
    process_path = os.path.abspath(process_path)

init()