import allure

from selene import browser, command


class AddtoFavorites:
    with allure.step("Добавление продукта в избранное"):
        def add_to_favorites(self):
            browser.element('[data-test-id="button__add-to-favorites"]').perform(command.js.scroll_into_view).click()
            browser.element('[data-test-id="button__add-to-favorites"]').click()
            return self


item_favorites = AddtoFavorites()