from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Urls
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators


class TestProfileAndNavigation:
    def test_go_to_personal_account(self, driver, registered_user):
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

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON)
        )

        driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()

        logout_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )
        assert logout_button.is_displayed()
        assert driver.current_url == Urls.PROFILE_URL

    def test_navigate_from_profile_to_constructor_via_button(self, driver, registered_user):
        driver.get(Urls.BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON)
        )

        driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )

        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        order_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON)
        )
        assert order_button.is_displayed()
        assert driver.current_url == Urls.BASE_URL

    def test_navigate_from_profile_to_constructor_via_logo(self, driver, registered_user):
        driver.get(Urls.BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON)
        )

        driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )

        driver.find_element(*MainPageLocators.LOGO).click()

        order_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON)
        )
        assert order_button.is_displayed()
        assert driver.current_url == Urls.BASE_URL
