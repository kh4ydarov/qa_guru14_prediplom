import allure

from selene import browser, have, command, be


class ChangeLanguage:
    with allure.step("Открывается сайт"):
        def open(self):
            browser.open_site()

    with allure.step("Переключаем язык"):
        def change_language_uz(self):
            browser.element('[data-test-id="text__selected-value"]').click()
            browser.element('[data-test-id="list__item"]').click()




# class EmptyWishes:
    def open(self):
        browser.open_site()

    def switching_page_wishes(self):
        browser.element('[data-test-id="button__wishes"]').click()
        # Проверяем, что мы на нужной странице
        browser.element('[data-test-id="list__products"]').should(be.visible)


# class CartSwitching:
    def switching_to_cart(self):
        browser.element('[data-test-id="button__cart"]').click()
        browser.element('[data-test-id="block__empty-page"]').should(be.visible)


# class SearchItem:
    def search_item(self, value):
        browser.element('[data-test-id="input__search"]').set_value(value).press_enter()
        browser.element('[data-test-id="text__product-name"]').should(be.visible)

    def regions(self, value):
        browser.element('[data-test-id="input__city-search"]').set_value(value)

