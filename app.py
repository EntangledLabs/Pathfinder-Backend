from flask import Flask
from flask_socketio import SocketIO, emit, join_room, leave_room, send
from dotenv import load_dotenv
import os

from puser import PathfinderUser, get_user
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

# Connection and authentication

@socketio.on('connect')
def on_connect(auth):
    pass

@socketio.on('disconnect')
def on_disconnect(auth):
    pass

# Channel connection

@socketio.on('join')
def on_join(data):
    pass

@socketio.on('leave')
def on_leave(data):
    pass


if __name__ == '__main__':
    socketio.run(app, debug=True)