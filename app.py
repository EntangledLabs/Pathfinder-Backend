from flask import Flask
from flask_socketio import SocketIO, emit, send
from dotenv import load_dotenv
import os

#++++++++++++++++++++++++++++++++++++++++++#
#              Initialization              #
#++++++++++++++++++++++++++++++++++++++++++#

# Get environment variables
load_dotenv()

# Flask server init
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SERVER_SECRET')

# WebSockets init
socketio = SocketIO(app)

#++++++++++++++++++++++++++++++++++++++++++#
#                 Routing                  #
#++++++++++++++++++++++++++++++++++++++++++#

@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"

#++++++++++++++++++++++++++++++++++++++++++#
#                WebSocket                 #
#++++++++++++++++++++++++++++++++++++++++++#

@socketio.on('send message')
def handle_message_send(data):
    emit('receive message', data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)