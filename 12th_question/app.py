# Build a Flask app that updates data in real-time using WebSocket connections.
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('joined')
def handle_joined(data):
    socketio.emit('message', data)

@socketio.on('message')
def handle_message(data):
    socketio.emit('message', data)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0",port=9000)