import random
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketServer(tornado.websocket.WebSocketHandler):
    client = set()

    def open(self):
        WebSocketServer.client.add(self)

    def on_close(self):
        WebSocketServer.client.remove(self)

    @classmethod
    def send_message(cls, message: str):
        print(f"Sending message to {len(cls.client)} clients")
        for client in cls.client:
            client.write_message(message)

class RandomWordSelector:
    def __init__(self, word_list):
        self.word_list = word_list

    def sample(self):
        return random.choice(self.word_list)

def main():
    app = tornado.web.Application(
        [(r"/websocket/", WebSocketServer)],
        websocket_ping_interval=10,
        websocket_ping_timeout=30,
    )
    app.listen(8888)
    io_loop = tornado.ioloop.IOLoop.current()
    word_selector = RandomWordSelector(['apple', 'banana', 'orange', 'grape', 'melon'])
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()), 3000)
    periodic_callback.start()
    io_loop.start()

if __name__ == "__main__":
    main()