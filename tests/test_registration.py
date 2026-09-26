from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Urls, UserData
from locators import RegisterPageLocators, LoginPageLocators


class TestRegistration:
    def test_registration_success(self, driver):
        driver.get(Urls.REGISTER_URL)

        email = UserData.generate_email()
        password = UserData.generate_valid_password()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)
        )
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Александр")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        ).is_displayed()

    def test_registration_invalid_password_show_error(self, driver):
        driver.get(Urls.REGISTER_URL)

        email = UserData.generate_email()
        invalid_password = UserData.generate_invalid_password()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)
        )
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Александр")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(invalid_password)

        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
        ).is_displayed()
