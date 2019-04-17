import tornado.web
import tornado.httpserver

class IndexHander(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('test')
        
app=tornado.web.Application([(r"/",IndexHander)])
server=tornado.httpserver.HTTPServer(app)
server.listen(8003)
server.start()
tornado.ioloop.IOLoop.current().start()