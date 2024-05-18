from model.item_search import search
from model.pages import page


def test_change_region():
    page.open_site()
    search.search_items()

