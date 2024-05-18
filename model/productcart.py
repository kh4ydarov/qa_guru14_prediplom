import allure

from selene import browser, command


class AddItem:
    with allure.step("Добавление продукта в корзину"):
        def add_item(self):
            browser.element('[data-tests-id="button__add-to-cart"]').perform(command.js.scroll_into_view).click()
            browser.element('[data-tests-id="button__add-to-cart"]').click()
            return self


item_to_cart = AddItem()
