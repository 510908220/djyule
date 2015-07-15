__author__ = 'hzz'

import tornado.web


class MusicItemModule(tornado.web.UIModule):
    def render(self, music_item):
        print music_item
        return self.render_string("modules/music_item.html", music_item=music_item)
