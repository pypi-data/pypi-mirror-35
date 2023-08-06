#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: 
# @file: manage.py
# @time: 2018/6/19 9:51
# @Software: PyCharm

from apihelper.settings import Config, Urls
import tornado.ioloop
import tornado.web
import tornado.httpserver


def make_app(urls=Urls):
    return tornado.web.Application(urls.urls, debug=Config.DEBUG)


def run(config=Config, urls=Urls):
    app = make_app(urls)
    server = tornado.httpserver.HTTPServer(app)
    server.bind(port=config.PORT, address=config.HOST)
    server.start(num_processes=config.NUM_PROCESSES)  # forks one process per cpu
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    run(config=Config, urls=Urls)
