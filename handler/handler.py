__author__ = 'hzz'

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class HomeHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        musics = yield tornado.gen.Task(self.db.query("SELECT * FROM musics"))
        self.render("home.html", musics=musics)


class LogHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        pass
        # client = tornado.httpclient.AsyncHTTPClient()
        # musics = yield tornado.gen.Task(self.db.query("SELECT * FROM musics"))
        # self.render("home.html", musics=musics)


class AdminHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        pass

    def post(self):
        pass
