# -*- coding:utf-8 -*-

import time
import conf
from helper import gunicorn_run, gunicorn_pids

def main():
    pids = gunicorn_pids(conf.APP)
    # exit if pids exists
    if len(pids):
        return "[%s] is running, pids = %s" % (conf.APP, str(pids))
    # start
    gunicorn_run(conf.APP, conf.WSGI, conf.PORT, conf.WORKER)
    time.sleep(1)
    pids = gunicorn_pids(conf.APP)
    # start success or not
    if not len(pids):
        return "[%s] start failed" % conf.APP
    return "[%s] start success, pids = %s" % str(pids)

if __name__ == "__main__":
    main()