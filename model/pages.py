import allure

from selene import browser, have, command, be


class OpenPage:
    with allure.step("Открывается сайт"):
        def open_site(self):
            browser.open("")
            return self

    with allure.step("Переход на страницу Избранные товары"):
        def open_wishes_items(self):
            browser.element('[data-test-id="button__wishes"]').click()
            return self

    with allure.step("Нажимаем на кнопку смена региона"):
        def open_modal_regions(self):
            browser.element('[data-test-id="button__select-city"]').click()
            return self

    with allure.step("Переход на корзину"):
        def open_carts_page(self):
            browser.element('[data-test-id="button__cart"]').click()
            return self


page = OpenPage()
