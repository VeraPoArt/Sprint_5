# Я уже написала фикстуру для регистрации и входа, поэтому буду ее использовать для теста для регистрации и входа  

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import (
    REGISTER_NAME_INPUT, 
    REGISTER_EMAIL_INPUT, 
    REGISTER_PASSWORD_INPUT, 
    REGISTER_SUBMIT_BUTTON,
    PASSWORD_ERROR_MESSAGE
)

def test_another_feature(driver, base_url, register_new_user, login_user):
    email, password = register_new_user  # Используем фикстуру для регистрации

    # Выполняем вход с помощью другой фикстуры и проверяем, что мы на странице личного кабинета
    login_user(email, password)
    assert driver.current_url == f"{base_url}account/profile"



def test_registration_with_invalid_password(driver, base_url, generate_credentials):

    # Проверка регистрации с некорректным паролем (менее 6 символов)

    email, _ = generate_credentials  # Игнорируем сгенерированный пароль
    invalid_password = "123"  # Пароль менее 6 символов
    # Открываем страницу регистрации
    driver.get(f"{base_url}register")
    
    # Заполняем форму регистрации
    name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(REGISTER_NAME_INPUT))
    name_input.send_keys(email.split('@')[0])
    
    email_input = driver.find_element(*REGISTER_EMAIL_INPUT)
    email_input.send_keys(email)

    password_input = driver.find_element(*REGISTER_PASSWORD_INPUT)
    password_input.send_keys(invalid_password)

    # Нажимаем кнопку "Зарегистрироваться"
    submit_button = driver.find_element(*REGISTER_SUBMIT_BUTTON)
    submit_button.click()

    # Проверяем наличие сообщения об ошибке
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located(PASSWORD_ERROR_MESSAGE))
    assert error_message.is_displayed()
