import tornado.web
from tornado.web import RequestHandler

class indexHandler(RequestHandler):
    def initialize(self,p1,p2):#接收传入参数
        self.p1=p1
        self.p2=p2
        
    def get(self,*args,**kwargs):
        print(self.p1,self.p2)
        self.write('index111')
        print('get flag:',self.get_query_argument('p3'))
        
class homeHandler(RequestHandler):
    def get(self,*args,**kwargs):
        self.write('home-handler')
        
class renderHandler(RequestHandler):
    def get(self,*args,**kwargs):
        list1=[{'name':'jack',"age":12},{"name":'rose',"age":22}]
        self.render('project1_file.html',list1=list1)