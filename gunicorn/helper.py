# -*- coding:utf-8 -*-

import os

def run(command, strip=True):
    lines = os.popen(command).readlines()
    if not strip:
        return "".join(r)
    lines = [line.strip() for line in lines]
    return "\n".join(lines)

def gunicorn_pids(app):
    try :
        lines = run("ps aux|grep gunicorn|grep '%s'|awk '{print $2}'" % app, strip=False)
        pids = [int(line.strip()) for line in lines]
    except:
        return []

def gunicorn_run(app, wsgi, port, worker):
    cmd_template = "gunicorn -D -w {worker} -b 0.0.0.0:{port} {app}:{wsgi}"
    command = cmd_template.format(worker=worker, port=port, app=app, wsgi=wsgi)
    temp_cwd = os.getcwd()
    work_dir = os.path.dirname(APP)
    os.chdir(work_dir)
    run(command)
    os.chdir(temp_cwd)
