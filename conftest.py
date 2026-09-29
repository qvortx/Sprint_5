import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Urls, UserData
from locators import RegisterPageLocators, LoginPageLocators


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def registered_user(driver):
    name = "Aleksandr"
    email = UserData.generate_email()
    password = UserData.generate_valid_password()

    driver.get(Urls.REGISTER_URL)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)
    )
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

    # Заменили обычный клик на ожидание кликабельности + JS-клик:
    register_button = WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON)
    )
    driver.execute_script("arguments[0].click();", register_button)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
    )

    return {
        "name": name,
        "email": email,
        "password": password
    }