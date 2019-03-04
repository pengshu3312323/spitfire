# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(__file__)

DEBUG = False

# 日志配置
LOG_FILE_NAME = BASE_DIR + '/log/error.log'
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# redis
if DEBUG:
    REDIS = {
      'host': 'localhost',
      'port': 6879,
      'password': 'hummel165',
    }
else:
    REDIS = {
        'host': '172.17.0.1',
        'port': 6879,
        'password': 'hummel165',
    }
