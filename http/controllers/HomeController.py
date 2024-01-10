import time
import appsettings
from ViewController import ViewController

from starter import MainHandler


class HomeController(ViewController):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.short_name = self.__class__.__name__.removesuffix('Controller').lower()

        
    def index(self) -> None :
        self.view_data = {'@timestamp': self.handler.session['timestamp']}
        if '@view_timestamp' in self.handler.session:
            self.view_data['@view_timestamp'] = self.handler.session['@view_timestamp']
        else:
            self.handler.session['@view_timestamp'] = time.time()
        self.return_view()

    def privacy(self) :
        self.return_view()


