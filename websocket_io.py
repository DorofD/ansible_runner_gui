from flask import Flask, render_template, copy_current_request_context
from flask_socketio import SocketIO, emit
from threading import Lock
import time
# from runner.runner import start_runner


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ewjkhfblweifh228'
socketio = SocketIO(app)


@socketio.on('connect_message')
def connect_message(data):
    print(data['data'])


@socketio.on('init_message')
def handle_message(data):
    thread = None
    thread_lock = Lock()

    @copy_current_request_context
    # def potok_sas():
    #     start_runner(emit_function=emit)
    @copy_current_request_context
    def potok_sas():
        time.sleep(3.5)
        emit('message', {'data': 'Message!'})
        time.sleep(3.5)
        emit('message', {'data': 'Message!'})
        time.sleep(3.5)
        emit('message', {'data': 'Message!'})

    print('received message: ' + data['data'])
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=potok_sas)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
