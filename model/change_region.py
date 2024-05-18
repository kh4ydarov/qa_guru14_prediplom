import allure

from selene import browser

class Region:
    with allure.step("Смена региона"):
        def change_region(self):
            browser.element('[data-tests-id="input__city-search"]').set_value("Ташкент").press_enter()
            browser.element('[data-tests-id="list__city"]').click()
            return self


region = Region()
