# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：fssc -> loggingConfig
@IDE    ：PyCharm
@Author ：Mr. Jiang
@Date   ：2020/7/21 10:26
@Desc   ：
==================================================
'''
import logging
import sys
import time
timeTuple = time.localtime()
localDate = time.strftime("%Y%m%d", timeTuple)
'''
    @Author:Mr. Jiang    
    @Date:2020/7/21 14:35
    @Desc:废弃
'''
# def getLog(msg):
#     logging.basicConfig(
#         level=logging.DEBUG, # 定义最低打印级别 DEBUG = 10 INFO = 20 WARNING = 30 ERROR = 40 CRITICAL = 50
#         # 输出位置
#         filename=f'../log/fssc-atuo-{localDate}.log', # 输出到文件
#         # stream=sys.stdout, # 输出到控制台
#         # format="%s", # 打印出日志所有内容
#         format="%(asctime)s [%(name)s] %(levelname)s : %(msg)s", # 日志格式
#         datefmt="%Y-%m-%d %H:%M:%S" # asctime 格式
#     )
#     logging.debug(msg)

loggingDic = {
    "version": 1,
    # "disable_existing_loggers": False,
    "formatters": { # 日志格式
        "default": { # 默认格式
            "format": "%(asctime)s [%(name)s] %(levelname)s : %(msg)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "simple": { # 简单格式
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(msg)s"
        }
    },
    "handlers": {# 句柄
        "console": { # 日志记录在控制台
            "class": "logging.StreamHandler",
            "level": "DEBUG", # 控制台记录DEBUG级别和更高级别日志
            "formatter": "simple",
            # "stream": "sys.stdout"
        },
        "info_file_handler": { # 日志记录在文件
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO", # 文件记录INFO级别和更高级别日志
            "formatter": "default",
            "filename": f"../log/fssc-info-{localDate}.log",
            "maxBytes": 1024*1024*5,
            "backupCount": 20,
            "encoding": "utf8"
        },
        # "error_file_handler": {
        #     "class": "logging.handlers.RotatingFileHandler",
        #     "level": "EEROR",
        #     "formatter": "simple",
        #     "filename": "errors.log",
        #     "maxBytes": 10485760,
        #     "backupCount": 20,
        #     "encoding": "utf8"
        # }
    },
    "loggers": {
        "root": {
            "level": "DEBUG", # 用户记录DEBUG级别和更高级别日志
            "handlers": [
                "console",
                "info_file_handler"
            ],
            "propagate": True
        }
    },
    # "root": {
    #     "level": "INFO",
    #     "handlers": [
    #         "console",
    #         "info_file_handler",
    #         "error_file_handler"
    #     ]
    # }
}