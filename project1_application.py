import tornado.web
import project1_index
import project1_config


class Application(tornado.web.Application):
    def __init__(self):
        handler=[
            (r"/",project1_index.indexHandler,{"p1":1,"p2":4}),
            (r"/home",project1_index.homeHandler),
            (r"/render",project1_index.renderHandler)
        ]
        super(Application,self).__init__(handler,**project1_config.setting)
    