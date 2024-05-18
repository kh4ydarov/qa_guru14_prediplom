from model.pages import page
from model.favourites_item import item_favorites




def test_switch_language():
    page.open_site()
    item_favorites.add_to_favorites()
