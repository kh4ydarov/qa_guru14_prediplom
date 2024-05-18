from model.pages import page
from model.change_language import change_languange


def test_switch_language():
    page.open_site()
    change_languange.switch_language()