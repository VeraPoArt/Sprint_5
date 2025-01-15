from selenium.webdriver.support.ui import WebDriverWait
from conftest import login_user
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import (
    LOGIN_BUTTON,
    HEADER_PROFILE_BUTTON,
    LOGIN_BUTTON_RECOVER,
    LOGIN_BUTTON_REG,

)
#вход по кнопке «Войти в аккаунт» на главной,
def test_login_flow(driver, base_url, register_new_user, login_user):
    # Регистрируем нового пользователя - фикстура register_new_user
    email, password = register_new_user
    wait = WebDriverWait(driver, 5)
    driver.get(f"{base_url}")

    # Нажимаем кнопку "Войти в аккаунт"
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))
    login_button.click()
    # Вводим email и пароль - фикстура login_user - проверяем через личный кабинет наличие элемента "Профиль"
    login_user(email, password)

#вход через кнопку «Личный кабинет»,
def test_login_lk(driver, base_url, register_new_user, login_user):
    # Регистрируем нового пользователя - фикстура register_new_user 
    email, password = register_new_user

    wait = WebDriverWait(driver, 10)
    driver.get(f"{base_url}")
    login_button = wait.until(EC.element_to_be_clickable(HEADER_PROFILE_BUTTON))
    login_button.click()
    
    # Вводим email и пароль - фикстура login_user - проверяем через личный кабинет наличие элемента "Профиль"
    login_user(email, password)

#вход через кнопку в форме регистрации,
def test_login_registration(driver, base_url, register_new_user, login_user):
    email, password = register_new_user
    wait = WebDriverWait(driver, 10)
    driver.get(f"{base_url}register")

    login_button_reg = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_REG))
    login_button_reg.click()

    # Вводим email и пароль - фикстура login_user - проверяем через личный кабинет наличие элемента "Профиль"
    login_user(email, password)

#вход через кнопку в форме восстановления пароля.
def test_login_recovery(driver, base_url, register_new_user, login_user):
    email, password = register_new_user
    wait = WebDriverWait(driver, 10)
    driver.get(f"{base_url}forgot-password")

    login_button_reg = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_BUTTON_RECOVER))
    login_button_reg.click()
    # Вводим email и пароль - фикстура login_user - проверяем через личный кабинет наличие элемента "Профиль"
    login_user(email, password)

