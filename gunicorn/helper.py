# -*- coding:utf-8 -*-

import os

def run(command, strip=True):
    lines = os.popen(command).readlines()
    if not strip:
        return "".join(lines)
    lines = [line.strip() for line in lines]
    return "\n".join(lines)

def gunicorn_pids(app):
    try :
        r = run("ps aux|grep gunicorn|grep ' %s'|grep -v 'ps aux'|awk '{print $2}'" % app)
        lines = r.split("\n")
        pids = [int(line) for line in lines]
        return pids
    except:
        return []

def gunicorn_run(workdir, module_wsgi, port, worker):
    cmd_template = "gunicorn -D -w {worker} -b 0.0.0.0:{port} {module_wsgi}"
    command = cmd_template.format(worker=worker, port=port, module_wsgi=module_wsgi)
    temp_cwd = os.getcwd()
    os.chdir(workdir)
    run(command)
    os.chdir(temp_cwd)
