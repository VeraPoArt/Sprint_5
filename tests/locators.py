from selenium.webdriver.common.by import By

# Кнопки регистрации и входа

LOGIN_BUTTON = (By.CSS_SELECTOR, ".button_button__33qZ0")  # Кнопка "Войти в аккаунт" на главной
LOGIN_BUTTON_REG = (By.LINK_TEXT, "Войти")  # Кнопка "Войти" на странице регистрации
LOGIN_BUTTON_RECOVER = (By.LINK_TEXT, "Войти")  # Кнопка "Войти" на странице восстановления пароля

# Поля формы регистрации
REGISTER_NAME_INPUT = (By.NAME, "name")  # Поле для имени при регистрации
REGISTER_EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")  # Поле для email при регистрации
REGISTER_PASSWORD_INPUT = (By.NAME, "Пароль")  # Поле для пароля при регистрации
REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, ".button_button__33qZ0")  # Кнопка "Зарегистрироваться"

# Поля формы входа
LOGIN_EMAIL_INPUT = (By.NAME, "name")  # Поле для email при входе
LOGIN_PASSWORD_INPUT = (By.NAME, "Пароль")  # Поле для пароля при входе
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]")  # Кнопка "Войти" на странице входа

# Элементы личного кабинета
HEADER_PROFILE_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")  # Кнопка "Личный кабинет" в хедере
PROFILE_LINK = (By.XPATH, "//a[contains(@href, '/account/profile')]")  # Ссылка "Профиль" в личном кабинете
LOGOUT_BUTTON = (By.XPATH, "//button[contains(.,'Выход')]")  # Кнопка "Выход" в личном кабинете

# Сообщения об ошибках
PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")

# Кнопки навигации на главной странице
HEADER_CONSTRUCTOR_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p")  # Кнопка «Конструктор»
HEADER_LOGO = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2 svg")  # Логотип Stellar Burgers

# Разделы конструктора
CONSTRUCTOR_BUNS_TAB = (By.XPATH, "//span[contains(.,'Булки')]")  # Вкладка «Булки»
CONSTRUCTOR_SAUCES_TAB = (By.XPATH, "//span[contains(.,'Соусы')]")  # Вкладка «Соусы»
CONSTRUCTOR_FILLINGS_TAB = (By.XPATH, "//span[contains(.,'Начинки')]")  # Вкладка «Начинки»


# Заголовки разделов после прокрутки
SECTION_BUNS = (By.XPATH, "//h2[contains(.,'Булки')]")  # Заголовок «Булки»
SECTION_SAUCES = (By.XPATH, "//h2[contains(.,'Соусы')]")  # Заголовок «Соусы»
SECTION_FILLINGS = (By.XPATH, "//h2[contains(.,'Начинки')]")  # Заголовок «Начинки»