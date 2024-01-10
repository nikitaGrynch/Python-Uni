import appsettings
from ViewController import ViewController

from starter import MainHandler
import sys
sys.path.append("./")
import dao


class ShopController(ViewController):
    
    def __init__(self, handler: MainHandler) -> None:
        self.handler = handler
        self.short_name = self.__class__.__name__.removesuffix('Controller').lower()
        self.view_path = f"{appsettings.VIEWS_PATH}/{self.short_name}"

        
    def index(self) -> None :
        products = dao.Products.get_all()
        if len(products) > 0:
            with open(f"{appsettings.VIEWS_PATH}/{self.short_name}/DisplayTemplates/product.html", encoding='utf-8') as tpl:
                data_template = tpl.read()
            product_views = []
            self.view_data = {}
            for product in products:
                product_view = data_template
                for k, v in product.items():
                    product_view = product_view.replace(f"{{{{{k}}}}}", str(v))
                product_views.append(product_view)
            self.view_data['@display_for_product'] = ''.join(product_views)

        self.return_view()

    def cart(self) :
        self.return_view()

    # def return_view(self, action_name: str) -> None:
    #     layout_name = f"{appsettings.VIEWS_PATH}/_layout.html"
    #     if not os.path.isfile(layout_name) or not os.path.isfile(action_name):
    #         print(("return_view::: file(s) not found: ", action_name, layout_name))
    #         self.handler.send_404()
    #         return
    #     with open(action_name, 'r') as action:
    #         with open(layout_name, 'r') as layout:
    #             self.handler.send_response(200)
    #             self.handler.send_header('Content-Type', 'text/html')
    #             self.handler.end_headers()
    #             self.handler.wfile.write(layout.read().replace('<!-- RenderBody -->', action.read()).encode())

