from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Urls
from locators import (
    MainPageLocators,
    LoginPageLocators,
    RegisterPageLocators,
    ForgotPasswordPageLocators
)


class TestLogin:
    def test_login_from_main_page_button(self, driver, registered_user):
        driver.get(Urls.BASE_URL)

        login_btn = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        )
        login_btn.click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON)
        )
        assert order_button.is_displayed()

    def test_login_from_profile_button_in_header(self, driver, registered_user):
        driver.get(Urls.BASE_URL)

        profile_btn = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.PROFILE_BUTTON)
        )
        profile_btn.click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON)
        )
        assert order_button.is_displayed()

    def test_login_from_registration_form(self, driver, registered_user):
        driver.get(Urls.REGISTER_URL)

        login_link = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)
        )
        login_link.click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON)
        )
        assert order_button.is_displayed()

    def test_login_from_forgot_password_form(self, driver, registered_user):
        driver.get(Urls.FORGOT_PASSWORD_URL)

        login_link = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)
        )
        login_link.click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON)
        )
        assert order_button.is_displayed()
