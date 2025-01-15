from tests.locators import HEADER_CONSTRUCTOR_BUTTON, HEADER_LOGO
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("button_selector", [
    HEADER_CONSTRUCTOR_BUTTON,
    HEADER_LOGO
])
def test_navigation_from_lk(driver, base_url, register_new_user, login_user, button_selector):

    #Тесты для перехода по кнопкам с Личного кабинета.
    #Параметризованный тест для кнопок "Конструктор" и "Логотип".

    email, password = register_new_user  # Используем фикстуру для регистрации
    # Выполняем вход с помощью другой фикстуры
    login_user(email, password)

    # Кликаем на кнопку
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_selector))
    button.click()

    # Проверяем, что текущий URL соответствует ожидаемому
    assert driver.current_url == f"{base_url}"


