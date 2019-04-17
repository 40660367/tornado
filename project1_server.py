import tornado.web
import tornado.ioloop
import tornado.httpserver
import project1_config
from project1_application import Application


app=Application()
server=tornado.httpserver.HTTPServer(app)
server.listen(project1_config.options['port'])
server.start()
tornado.ioloop.IOLoop.current().start()