from model.change_region import region
from model.pages import page


def test_change_region():
    page.open_site()
    page.open_modal_regions()
    region.change_region()

