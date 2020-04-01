import tornado.ioloop
import tornado.web
import os
import json

class BaseHandler(tornado.web.RequestHandler):
    #blog.csdn.net/moshowgame 解决跨域问题
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',#'*')
                        'authorization, Authorization, Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')

class AjaxHandler(BaseHandler):
    def post(self):
        #h = self.get_argument('username')
        #h1 = self.get_argument('password')
        h = str(self.request.body,encoding="utf-8")
        h_new = h.split('.',1)
        username = h_new[0]
        password = h_new[1]
        print(username)
        print(password)
        with open("username.txt","r") as f1:
            j1 =f1.read()
        print(j1)
        with open("password.txt","r") as f2:
            j2 = f2.read()
        print(j2)
        if username == j1 and password == j2:
            self.write("http://www.baidu.com/")
        else:
            self.write("http://www.hao123.com/")
        #print(h1)

class ZuobiaoHandler(BaseHandler):
    def post(self):
        new = str(self.request.body,encoding="utf-8")
        print(new)
        
application = tornado.web.Application([
    (r"/check", AjaxHandler),
    (r"/zuobiao",ZuobiaoHandler),
    ])

if __name__ == '__main__':
    application.listen(20867)
    tornado.ioloop.IOLoop.instance().start()
