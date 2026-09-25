from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Urls
from locators import MainPageLocators


class TestConstructor:
    def test_switch_to_sauces_tab(self, driver):
        driver.get(Urls.BASE_URL)

        sauces_tab = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        )
        sauces_tab.click()

        active_tab = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ACTIVE_TAB)
        )
        assert active_tab.text == "Соусы"

    def test_switch_to_fillings_tab(self, driver):
        driver.get(Urls.BASE_URL)

        fillings_tab = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)
        )
        fillings_tab.click()

        active_tab = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ACTIVE_TAB)
        )
        assert active_tab.text == "Начинки"

    def test_switch_to_buns_tab(self, driver):
        driver.get(Urls.BASE_URL)

        sauces_tab = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        )
        sauces_tab.click()

        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(MainPageLocators.ACTIVE_TAB, "Соусы")
        )

        buns_tab = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.BUNS_TAB)
        )
        buns_tab.click()

        active_tab = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ACTIVE_TAB)
        )
        assert active_tab.text == "Булки"
