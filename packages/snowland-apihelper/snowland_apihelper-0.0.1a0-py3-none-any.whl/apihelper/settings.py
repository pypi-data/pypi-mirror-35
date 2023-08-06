#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: settings.py
# @time: 2018/9/8 0:53
# @Software: PyCharm


from apihelper.handlers import HelloWorldHandler

class Config(object):
    DEBUG = True
    HOST = "127.0.0.1"
    PORT = 10008
    NUM_PROCESSES = 1

class Urls(object):
    urls = [

        (r"/helloworld", HelloWorldHandler.HelloWorldHandler),
    ]
