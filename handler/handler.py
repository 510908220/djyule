__author__ = 'hzz'

import tornado.web
import tornado.gen

import config
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class HomeHandler(BaseHandler):
    def get(self, page_id):
        musics = self.db[config.TB_MUSIC].find()

        if not page_id:
            page_id = 1
        self.render("home.html", musics=musics, page_id = page_id, max_page = 50)


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
