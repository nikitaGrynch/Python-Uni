from ViewController import ViewController
import appsettings
import sys
sys.path.append("./")
import dao

class CartController(ViewController):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def index(self):
        cart_items = dao.Cart.get_items(id_user="100637654525149186")
        total_cnt = 0
        total_price = 0
        if len(cart_items) != 0:
            with open(f"{appsettings.VIEWS_PATH}/cart/DisplayTemplates/cart-item.html", encoding='utf-8') as tpl:
                data_template = tpl.read()
                cart_item_views = []
                for cart_item in cart_items:
                    cart_item_view = data_template
                    total_cnt += cart_item['cnt']
                    total_price += cart_item['cnt'] * cart_item['price']
                    for k, v in cart_item.items():
                        cart_item_view = cart_item_view.replace(f"{{{{{k}}}}}", str(v))
                    cart_item_views.append(cart_item_view)
            self.view_data['@display_for_cart'] = ''.join(cart_item_views)
            self.view_data['@total_cnt'] = str(total_cnt)
            self.view_data['@total_price'] = str(total_price)
        # print(list(cart_items))
        self.return_view()