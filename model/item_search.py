import allure

from selene import browser, be


class Search:
    with allure.step("Поиск продукта"):
        def search_items(self):
            browser.element('[data-tests-id="input__search"]').set_value("Murphy").press_enter()
            browser.element('[data-tests-id="text__product-name"]').should(be.visible)
            return self


search = Search()
