import inspect
import json
import time
import uuid
import appsettings

from http.server import HTTPServer, BaseHTTPRequestHandler
import importlib
import os
import sys
sys.path.append(appsettings.CONTROLLERS_PATH)
# import HomeController

class MainHandler(BaseHTTPRequestHandler):
    sessions = dict()
    def do_GET(self) -> None:
        url_parts = self.path.split('?')
        if(len(url_parts) > 2):
            self.send_404()
            return
        path = url_parts[0]
        query_string = url_parts[1] if len(url_parts) == 2 else None
        filename = f"{appsettings.WWWROOT_PATH}/{path}"
        if os.path.isfile(filename):
            self.flush_file(filename)
            return
        
        # work with cookies
        self.response_headers = dict()
        self.cookies = dict(cookie.split('=') for cookie in self.headers['Cookie'].split('; ')) if 'Cookie' in self.headers else {}

        #work with session
        self.session = None
        session_id = self.cookies['session_id'] if 'session_id' in self.cookies else str(uuid.uuid1())
        if not session_id in MainHandler.sessions :
            # create new session
            session_id = str(uuid.uuid1())
            MainHandler.sessions[session_id] = {
                'timestamp': time.time(),
                'session_id': session_id
            }
            self.response_headers['Set-Cookie'] = f'session_id={session_id}'
        self.session = MainHandler.sessions[session_id]
        print(self.session)


        path_parts = path.split('/')
        controller_name = (path_parts[1].capitalize() if path_parts[1] != '' else 'Home') + 'Controller'
        action_name = path_parts[2].lower() if len(path_parts) > 2 and path_parts[2] != '' else 'index'
        try:
            controller_module = importlib.import_module(controller_name)
            controller_class = getattr(controller_module, controller_name)
            controller_object = controller_class(handler=self)
            controller_action = getattr(controller_object, action_name)
        except Exception as err:
            print(err)
            controller_action = None

        if controller_action is None:
            self.send_404()
            return
        controller_action()
        return
    

    def return_view(self, action_name = None) -> None:
        layout_name = f"{appsettings.VIEWS_PATH}/_layout.html"
        controller_object = inspect.currentframe().f_back.f_locals['self']
        view_path = f"{appsettings.VIEWS_PATH}/{controller_object.short_name}"
        action_name = f"{view_path}/{inspect.currentframe().f_back.f_code.co_name}.html"
        if not os.path.isfile(layout_name) or not os.path.isfile(action_name):
            print(("return_view::: file(s) not found: ", action_name, layout_name))
            self.send_404()
            return
        with open(action_name, 'r') as action:
            with open(layout_name, 'r') as layout:
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                for k, v in self.response_headers.items() :
                    self.send_header(k, v)
                self.end_headers()
                self.wfile.write(layout.read().replace('<!-- RenderBody -->', action.read()).encode())

    def flush_file(self, filename) -> None:
        if '..' in filename or not os.path.isfile(filename):
            self.send_404()
            return  
        ext = filename.split('.')[-1] if '.' in filename else ''
        if ext in ('html', 'css') :
            content_type = 'text/' + ext
        elif ext == 'js':
            content_type = 'text/javascript'
        elif ext == 'ico':
            content_type = 'image/x-icon'
        elif ext in ('png', 'bmp', 'gif'):
            content_type = 'image/' + ext
        elif ext in ('py', 'jss', 'php', 'exe', 'env', 'log', 'bat', 'cmd', 'sql', 'gitignore') :
            self.send_404()
            return
        else:
            content_type = 'application/octet-stream'
        
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.end_headers()

        with open(filename, 'rb') as file:
            self.wfile.write(file.read())
        return
    
    def send_404(self) -> None:
        self.send_response(404)
        self.send_header("Status", "404 Not Found")
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Requested page not found')
        return

    def log_request(self, code: int | str = '-', size: int | str = '-') -> None:
       return None

def main() -> None:
    server = HTTPServer(('127.0.0.1', 4433), MainHandler)
    try:
        # load session from json file
        try:
            with(open("sessions.json", mode="r", encoding="utf-8")) as file:
                MainHandler.sessions = json.loads(file.read())
        except IOError as err:
            print("Error: ", err)
        print('Server starting...')
        server.serve_forever()
    except:
        # save session to json file
        try:
            with(open("sessions.json", mode="w", encoding="utf-8")) as file:
                file.write(json.dumps(MainHandler.sessions))
        except IOError as err:
            print("Error: ", err)
        print('Server stopped')

if __name__ == '__main__':
    main()