from flask import Flask, render_template
from flask_websockets import WebSockets, ws, has_socket_context


app = Flask(__name__)
sockets = WebSockets(app)


@sockets.on_open
def boba():
    if has_socket_context():
        while True:
            message = input('Enter message: ')
            if message == 'stop':
                ws.close()
                break
            ws.send(message)


@sockets.on_message
def echo(message):
    print(message)
    return 'Hello from Server!'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(
        ('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
