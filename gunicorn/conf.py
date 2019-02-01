# -*- coding:utf-8 -*-

WORKDIR = "../server/"
MODULE_WSGI = "entry:app"
MODULE = "entry"
WSGI = "app"
PORT = 5000

# 初始化
import os
from multiprocessing import cpu_count

WORKDIR = os.path.abspath(WORKDIR)
CPU_CORE = cpu_count()
WORKER = 2 * CPU_CORE + 1
