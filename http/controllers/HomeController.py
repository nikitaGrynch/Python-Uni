import appsettings

from starter import MainHandler
import inspect
import os


class HomeController:
    
    def __init__(self, handler: MainHandler) -> None:
        self.handler = handler
        self.short_name = self.__class__.__name__.removesuffix('Controller').lower()
        self.view_path = f"{appsettings.VIEWS_PATH}/{self.short_name}"

        
    def index(self) -> None :
        self.return_view(f"{self.view_path}/{inspect.currentframe().f_code.co_name}.html")

    def privacy(self) :
        self.return_view(f"{self.view_path}/{inspect.currentframe().f_code.co_name}.html")

    def return_view(self, action_name: str) -> None:
        layout_name = f"{appsettings.VIEWS_PATH}/_layout.html"
        if not os.path.isfile(layout_name) or not os.path.isfile(action_name):
            print(("return_view::: file(s) not found: ", action_name, layout_name))
            self.handler.send_404()
            return
        with open(action_name, 'r') as action:
            with open(layout_name, 'r') as layout:
                self.handler.send_response(200)
                self.handler.send_header('Content-Type', 'text/html')
                self.handler.end_headers()
                self.handler.wfile.write(layout.read().replace('<!-- RenderBody -->', action.read()).encode())

