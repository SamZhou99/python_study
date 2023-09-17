import tornado.ioloop
import tornado.web
import tornado.websocket
import datetime, time


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self, *args, **kwargs):
        pass


users = set()
index = 0


class ChatHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args, **kwargs):
        """客户端连接"""
        global index
        users.add(self)
        # time.sleep(1)
        index = index + 1
        self.id = index
        print("open...", self.id)
        # print(self.request)
        self.write_message("欢迎第 {} 位客人！".format(index))

    def on_message(self, message):
        """有消息到达"""
        now = datetime.datetime.now()
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        print("收到消息", content, message)
        self.write_message(content)
        # 广播给其他人，除了自己。
        for client in users:
            if client == self:
                continue
            client.write_message(content)

    def on_close(self):
        """客户端主动关闭连接"""
        print("close...", self.id)
        users.remove(self)


st = {
    "template_path": "template",  # 模板路径配置
    "static_path": "static",
}

# 路由映射   匹配执行，否则404
application = tornado.web.Application(
    [
        # ("/", MainHandler),
        # ("/", ChatHandler),
        ("/wschat", ChatHandler),
    ],
    **st
)

if __name__ == "__main__":
    application.listen(8090)

    # io多路复用
    tornado.ioloop.IOLoop.instance().start()
