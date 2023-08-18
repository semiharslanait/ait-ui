import os
import tempfile
from http.cookies import SimpleCookie

from flask import Flask, request, send_from_directory, abort
from flask_cors import CORS
from flask_socketio import SocketIO

from .core import Session, clear_index

flask_app = Flask(__name__)
socketio = SocketIO(flask_app)

# Global definitions for convenience
server = flask_app
web_socket = socketio
web_request = request
Session.socket = socketio

CORS(flask_app)

ui_root = None

dir_routes = {}
sessions = {}
un_init_sessions = []

@socketio.on('connect')
def handle_client_connect():
    print('Socket connected')
    cookie_str = request.args.get('cookie')

    cookies_dict = {}
    if cookie_str and cookie_str.strip():
        parsed_cookie = SimpleCookie()
        try:
            parsed_cookie.load(cookie_str)
            cookies_dict = {key: morsel.value for key, morsel in parsed_cookie.items()}
        except Exception as e:
            print(f"Error parsing cookie: {e}")

    session_instance = un_init_sessions.pop()
    session_instance.cookies = cookies_dict

    sessions[request.sid] = session_instance
    session_instance.init(request.sid)
    session_instance.socket.emit('afterconnect', {'message': 'Connection initialized'})

@socketio.on('from_client')
def handle_from_client(msg):
    Session.current_session = sessions[request.sid]
    Session.current_session.clientHandler(msg['id'], msg['value'], msg['event_name'])

@flask_app.route('/')
def home():
    session = Session(ui_root)
    un_init_sessions.append(session)
    session.clear_index()
    ui_root()
    return session.get_index()

@flask_app.route('/<path:path>')
def files(path):
    return send_from_directory("static", path)

@flask_app.route('/file-upload', methods=['POST'])
def upload():
    id = request.form['id']
    file = request.files['file']
    uid = request.form['uid']
    if file:
        file.save(os.path.join(tempfile.gettempdir(), uid))
    return 'File uploaded successfully.'    #TODO: add error handling here

@flask_app.route('/js/<path:path>')
def js_files(path):
    return send_from_directory("js", path)

def add_static_route(route, osDirPath):
    print("Route Path:",osDirPath)  # Ensure the path is correct
    dir_routes[route] = osDirPath

@flask_app.route('/<route>/<path:file_path>')
def custom_files(route, file_path):
    if route not in dir_routes:
        abort(404)
    return send_from_directory(dir_routes[route], file_path)

def add_custom_route(route, ui_class, middlewares=[]):
    @flask_app.route(route, endpoint=f"{ui_class.__name__}")
    def custom_route_func():
        session = Session(ui_class)
        un_init_sessions.append(session)
    
        # Apply all middleware decorators
        session.clear_index()
        ui_class()
        wrapped_func = session.get_index
        for middleware in reversed(middlewares):
            wrapped_func = middleware(wrapped_func)

        return wrapped_func()
    
    return custom_route_func

def run(ui = None, port=5000, debug=True):
    global ui_root
    assert ui is not None, "ui is None"
    ui_root = ui
    flask_app.run(host="0.0.0.0",port=port, debug=debug)

if __name__ == '__main__':
    run()
