# -*- coding:utf-8 -*-

APP = ""
WSGI = "APP"
PORT = 5000

# 初始化
import os
from multiprocessing import cpu_count

APP = os.path.abspath(APP)
WORK_DIR = os.path.dirname(APP)
CPU_CORE = cpu_count()
WORKER = 2 * CPU_CORE + 1