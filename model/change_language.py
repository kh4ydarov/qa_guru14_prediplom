import allure

from selene import browser


class ChangeLanguage:
    with allure.step("Переключаем язык"):
        def switch_language(self):
            browser.element('[data-test-id="text__selected-value"]').click()
            browser.element('[data-test-id="list__item"]').click()


change_languange = ChangeLanguage()