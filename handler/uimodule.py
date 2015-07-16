__author__ = 'hzz'

import tornado.web


class MusicItemModule(tornado.web.UIModule):
    def render(self, music_item):
        new_music_item = {}
        del music_item[u"_id"]
        for k in music_item:
            new_music_item[k.encode("utf-8")] = music_item[k].encode("utf-8")

        print new_music_item
        return self.render_string("modules/music_item.html", music_item=new_music_item)
