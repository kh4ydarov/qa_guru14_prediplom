from model.pages import page
from model.productcart import item_to_cart




def test_item_addingtocart():
    page.open_site()
    item_to_cart.add_item()