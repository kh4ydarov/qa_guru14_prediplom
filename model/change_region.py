import allure

from selene import browser, have, command, be


class Region:
    with allure.step("Смена региона"):
        def change_region(self):
            browser.element('[data-test-id="button__select-city"]').click()
            browser.element('[data-test-id="input__city-search"]').set_value("Ташкент").press_enter()
            browser.element('[data-test-id="block__city"]').click()
            return self


region = Region()
