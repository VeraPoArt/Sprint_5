import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import HEADER_PROFILE_BUTTON, PROFILE_LINK, REGISTER_NAME_INPUT, REGISTER_EMAIL_INPUT, REGISTER_PASSWORD_INPUT, REGISTER_SUBMIT_BUTTON, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_SUBMIT_BUTTON

@pytest.fixture(scope="function")
def base_url():
    return "https://stellarburgers.nomoreparties.site/"

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome, firefox"
    )

@pytest.fixture(scope="function")
def driver(request):

    browser = request.config.getoption("--browser")

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def generate_credentials(cohort_number, domain="yandex.ru"):
    # Генерация уникального email и случайного пароля
    name = ''.join(random.choices(string.ascii_lowercase, k=5))
    surname = ''.join(random.choices(string.ascii_lowercase, k=5))
    random_number = ''.join(random.choices(string.digits, k=3))
    email = f"{name}_{surname}_{cohort_number}_{random_number}@{domain}"
    password_length = 8
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=password_length))
    return email, password

@pytest.fixture(scope="function")
def cohort_number():
    return "17"  # Укажите номер когорты, который вам нужен

@pytest.fixture(scope="function")
def register_new_user(driver, base_url, generate_credentials):
    """
    Фикстура для регистрации нового пользователя.
    Возвращает email и пароль зарегистрированного пользователя.
    """
    email, password = generate_credentials

    wait = WebDriverWait(driver, 10)

    # Открываем страницу регистрации
    driver.get(f"{base_url}register")

    # Заполняем форму регистрации
    name_input = wait.until(EC.presence_of_element_located(REGISTER_NAME_INPUT))
    name_input.send_keys(email.split('@')[0])

    email_input = wait.until(EC.presence_of_element_located(REGISTER_EMAIL_INPUT))
    email_input.send_keys(email)

    password_input = wait.until(EC.presence_of_element_located(REGISTER_PASSWORD_INPUT))
    password_input.send_keys(password)

    # Нажимаем кнопку "Зарегистрироваться"
    submit_button = wait.until(EC.element_to_be_clickable(REGISTER_SUBMIT_BUTTON))
    submit_button.click()

    # Ждем перехода на страницу входа
    wait.until(EC.url_contains('/login'))

    return email, password

@pytest.fixture(scope="function")
def login_user(driver, base_url):
    """
    Фикстура для входа пользователя.
    Принимает email и пароль через параметры.
    """
    def _login(email, password):
        wait = WebDriverWait(driver, 10)

        # Выполняем вход
        email_input = wait.until(EC.presence_of_element_located(LOGIN_EMAIL_INPUT))
        email_input.send_keys(email)

        password_input = wait.until(EC.presence_of_element_located(LOGIN_PASSWORD_INPUT))
        password_input.send_keys(password)

        login_button = wait.until(EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON))
        login_button.click()

        # Переходим в личный кабинет для проверки успешного входа
        profile_button = wait.until(EC.element_to_be_clickable(HEADER_PROFILE_BUTTON))
        profile_button.click()
        # Проверяем наличие элемента "Профиль" в личном кабинете
        assert wait.until(EC.presence_of_element_located(PROFILE_LINK))

    return _login


