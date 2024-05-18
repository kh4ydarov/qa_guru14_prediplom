import allure

from selene import browser, have, command, be


class Search:
    with allure.step("Поиск продукта"):
        def search_items(self):
            browser.element('[data-test-id="input__search"]').set_value("Murphy").press_enter()
            browser.element('[data-test-id="text__product-name"]').should(be.visible)
            return self


search = Search()
