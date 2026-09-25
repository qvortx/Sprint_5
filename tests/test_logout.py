from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Urls
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators


class TestLogout:
    def test_logout_from_profile(self, driver, registered_user):
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

        logout_btn = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        )
        logout_btn.click()

        login_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        assert login_button.is_displayed()
        assert driver.current_url == Urls.LOGIN_URL
