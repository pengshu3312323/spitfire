#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web

from urls import handlers


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('test')


def make_app():
    return tornado.web.Application(
        [
            (r'/', MainHandler),
        ]
    )


if __name__ == '__main__':
    app = make_app()
    app.listen(8002)
    tornado.ioloop.IOLoop.current().start()
