from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']/parent::a")
    LOGO = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]/a")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']/parent::div")

    ACTIVE_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]//span")


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")


class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")


class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
