from flask import Flask, session
from flask_socketio import SocketIO, emit
from flask_login import LoginManager
from dotenv import load_dotenv
import os

#++++++++++++++++++++++++++++++++++++++++++#
#              Initialization              #
#++++++++++++++++++++++++++++++++++++++++++#

# Get environment variables
load_dotenv()

# Flask server init
app = Flask(__name__)
app.secret_key = bytes(os.getenv('SERVER_SECRET'))

# WebSockets init
socketio = SocketIO(app)

# Flask-Login init
login_manager = LoginManager()
login_manager.init_app(app)

#++++++++++++++++++++++++++++++++++++++++++#
#                 Routing                  #
#++++++++++++++++++++++++++++++++++++++++++#

@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"

#++++++++++++++++++++++++++++++++++++++++++#
#                WebSocket                 #
#++++++++++++++++++++++++++++++++++++++++++#

@socketio.event
def my_event(message):
    emit('my response', {'data': 'got it!'})

#++++++++++++++++++++++++++++++++++++++++++#
#              Authentication              #
#++++++++++++++++++++++++++++++++++++++++++#