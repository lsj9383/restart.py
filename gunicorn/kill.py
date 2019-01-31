# -*- coding:utf-8 -*-

import time
import conf
from helper import run, gunicorn_pids

def main():
    pids = gunicorn_pids(conf.APP)
    # exit if pids exists
    if not len(pids):
        return "[%s] not exists"
    # kill all
    for pid in pids:
        run("kill -s QUIT %s")
    time.sleep(1)

if __name__ == "__main__":
    main()