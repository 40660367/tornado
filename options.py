import tornado.web
import tornado.httpserver
import tornado.options

tornado.options.define("port",default=8009,type=int)
tornado.options.define("list",default=[],type=str,multiple=True)


class IndexHander(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('test')
        self.write('test')
        
app=tornado.web.Application([(r"/",IndexHander)])
server=tornado.httpserver.HTTPServer(app)

tornado.options.parse_command_line()
server.listen(tornado.options.options.port)
server.start()
tornado.ioloop.IOLoop.current().start()