# -*- coding:utf-8 -*-

import time
import conf
from helper import gunicorn_run, gunicorn_pids

def main():
    pids = gunicorn_pids(conf.MODULE_WSGI)
    # exit if pids exists
    if len(pids):
        return "[%s] is running, pids = %s" % (conf.MODULE_WSGI, str(pids))
    # start
    gunicorn_run(conf.WORKDIR, conf.MODULE_WSGI, conf.PORT, conf.WORKER)
    time.sleep(1)
    pids = gunicorn_pids(conf.MODULE_WSGI)
    # start success or not
    if not len(pids):
        return "[%s] start failed" % conf.MODULE_WSGI
    return "[%s] start success, pids = %s" % (conf.MODULE_WSGI, str(pids))

if __name__ == "__main__":
    resp = main()
    print(resp)
