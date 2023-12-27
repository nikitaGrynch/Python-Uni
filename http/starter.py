import appsettings

from http.server import HTTPServer, BaseHTTPRequestHandler
import importlib
import os
import sys
sys.path.append(appsettings.CONTROLLERS_PATH)
# import HomeController

class MainHandler(BaseHTTPRequestHandler):
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
        print('Server starting...')
        server.serve_forever()
    except:
        print('Server stopped')

if __name__ == '__main__':
    main()