import random


class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru/"
    LOGIN_URL = f"{BASE_URL}login"
    REGISTER_URL = f"{BASE_URL}register"
    FORGOT_PASSWORD_URL = f"{BASE_URL}forgot-password"
    PROFILE_URL = f"{BASE_URL}account/profile"


class UserData:
    COHORT_NUMBER = 55

    @staticmethod
    def generate_email():
        random_digits = random.randint(100, 999)
        return f"aleksandr_khatskevich_{UserData.COHORT_NUMBER}_{random_digits}@yandex.ru"

    @staticmethod
    def generate_valid_password():
        return f"Pass{random.randint(100000, 999999)}"

    @staticmethod
    def generate_invalid_password():
        return "12345"
