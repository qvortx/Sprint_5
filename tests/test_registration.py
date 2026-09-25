from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Urls, UserData
from locators import RegisterPageLocators, LoginPageLocators


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(Urls.REGISTER_URL)

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)
        )

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Aleksandr")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(UserData.generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(UserData.generate_valid_password())

        register_button = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(RegisterPageLocators.REGISTER_BUTTON)
        )
        driver.execute_script("arguments[0].click();", register_button)

        login_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        assert login_button.is_displayed()

    def test_registration_invalid_password_show_error(self, driver):
        driver.get(Urls.REGISTER_URL)

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)
        )

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Aleksandr")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(UserData.generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(UserData.generate_invalid_password())

        register_button = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(RegisterPageLocators.REGISTER_BUTTON)
        )
        driver.execute_script("arguments[0].scrollIntoView();", register_button)
        
        register_button.click()

        error_message = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
        )
        assert error_message.is_displayed()
        assert error_message.text == "Некорректный пароль"
