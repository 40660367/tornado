import tornado.web
import tornado.ioloop

class IndexHander(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('test')
        
app=tornado.web.Application([(r"/",IndexHander)])
app.listen(8001)
tornado.ioloop.IOLoop.current().start()