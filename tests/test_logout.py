
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import LOGOUT_BUTTON

def test_from_lk_to_constructor(driver, base_url, register_new_user, login_user):
    email, password = register_new_user  # Используем фикстуру для регистрации

    # Выполняем вход с помощью другой фикстуры
    login_user(email, password)

    # Кликаем на кнопку "Выход"
    logout_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(LOGOUT_BUTTON))
    logout_button.click()

    # Проверяем, что текущий URL соответствует ожидаемому
    WebDriverWait(driver, 10).until(EC.url_to_be(f"{base_url}login"))
    assert driver.current_url == f"{base_url}login"

