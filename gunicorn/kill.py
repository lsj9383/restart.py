# -*- coding:utf-8 -*-

import time
import conf
from helper import run, gunicorn_pids

def main():
    pids = gunicorn_pids(conf.MODULE_WSGI)
    # exit if pids exists
    if not len(pids):
        return "[%s] not exists" % conf.MODULE_WSGI
    # kill all
    for pid in pids:
        run("kill -s QUIT %s" % pid)
    time.sleep(1)
    pids = gunicorn_pids(conf.MODULE_WSGI)
    if not len(pids):
        return "[%s] kill success" % conf.MODULE_WSGI
    return "[%s] kill failed, pids = [%s]" % (conf.MOUDLE_WSGI, str(pids))

if __name__ == "__main__":
    resp = main()
    print(resp)
