# Переход в личный кабинет 
# Проверь переход по клику на «Личный кабинет».
# 1 проверка СО страницы {base_url} без авторизации в личном кабинете происходит переход на {base_url}login
# 2 проверка СО страницы {base_url}feed без авторизации в личном кабинете происходит переход на {base_url}login
# 3 проверка СО страницы {base_url}login без авторизации в личном кабинете происходит переход на {base_url}login
# 4 проверка СО страницы {base_url}register без авторизации в личном кабинете происходит переход на {base_url}login
# 5 проверка СО страницы {base_url}forgot-password без авторизации в личном кабинете происходит переход на {base_url}login

# 1 проверка СО страницы {base_url}profile с авторизацией  в личном кабинете происходит переход на {base_url}profile
# 2 проверка СО страницы {base_url}feed с авторизацией  в личном кабинете происходит переход на {base_url}profile


import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import HEADER_PROFILE_BUTTON, PROFILE_LINK

@pytest.mark.parametrize("start_url", [
    "",  # Главная страница
    "feed",  # Страница ленты
    "login",  # Страница входа
    "register",  # Страница регистрации
    "forgot-password"  # Страница восстановления пароля
])
def test_login_noauth(driver, base_url, start_url):
    wait = WebDriverWait(driver, 5)
    driver.get(f"{base_url}{start_url}")
    
    # Переходим к кнопке "Личный Кабинет" и кликаем
    lk_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HEADER_PROFILE_BUTTON))
    lk_button.click()
    
    # Проверяем, что текущий URL соответствует ожидаемому
    assert driver.current_url == f"{base_url}login"

@pytest.mark.parametrize("start_url", [
    "",  # Главная страница
    "feed",  # Страница ленты

])
def test_login_auth(driver, base_url, start_url, register_new_user, login_user):

    email, password = register_new_user  # Используем фикстуру для регистрации
    # Выполняем вход с помощью другой фикстуры
    login_user(email, password)
    driver.get(f"{base_url}{start_url}")
    # Переходим к кнопке "Личный Кабинет" и кликаем
    lk_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HEADER_PROFILE_BUTTON))
    lk_button.click()
    # Проверяем, что текущий URL соответствует ожидаемому
    assert driver.current_url == f"{base_url}account/profile"
