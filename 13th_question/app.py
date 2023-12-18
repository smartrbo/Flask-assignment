# 13. Implement notifications in a Flask app using websockets to notify users of updates.
from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('A user connected')

@socketio.on('notification')
def send_notification(data):
    message = data['message']
    socketio.emit('notification', {'message': message}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0",port=7000)