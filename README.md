# Sprint_5 - Автотесты для Stellar Burgers

## Описание проекта

Данный проект содержит автотесты для сервиса Stellar Burgers, разработанные с использованием Selenium WebDriver и pytest на языке Python.

## Структура проекта
```
Sprint_5/
│
├── tests/
│   ├── test_registration.py
│   ├── test_login.py
│   ├── test_navigation_to_personal_account.py
│   ├── test_navigation_from_personal_account.py
│   ├── test_logout.py
│   └── test_constructor_sections.py
│
├── conftest.py
├── requirements.txt
├── README.md
└── .gitignore
```

- `tests/`: Директория, содержащая все тестовые файлы.
  - `test_registration.py`: Тесты для регистрации.
  - `test_login.py`: Тесты для входа.
  - `test_navigation_to_personal_account.py`: Тесты перехода в личный кабинет.
    - **Описание тестов**: 
      - Проверка перехода на страницу входа (`{base_url}login`) без авторизации с различных страниц:
        1. С главной страницы (`{base_url}`).
        2. Со страницы ленты (`{base_url}feed`).
        3. Со страницы входа (`{base_url}login`).
        4. Со страницы регистрации (`{base_url}register`).
        5. Со страницы восстановления пароля (`{base_url}forgot-password`).
      - Проверка перехода на страницу профиля (`{base_url}profile`) с авторизацией:
        1. Со страницы профиля (`{base_url}profile`).
        2. Со страницы ленты (`{base_url}feed`).
  - `test_navigation_from_personal_account.py`: Тесты перехода из личного кабинета в конструктор.
  - `test_logout.py`: Тесты для выхода из аккаунта.
  - `test_constructor_sections.py`: Тесты для разделов конструктора.
- `locators.py`: Файл с описанием всех локаторов, используемых в тестах.
- `conftest.py`: Файл с фикстурами для pytest.
- `README.md`: Описание проекта, инструкции по запуску тестов и другая полезная информация.
- `.gitignore`: Файл для исключения лишних файлов из коммита.
- `requirements.txt`: Файл с зависимостями проекта.

## Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone <URL вашего репозитория>
   cd Sprint_5
   ```

2. **Создайте и активируйте виртуальное окружение:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```

3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Скачайте драйверы браузеров и поместите их в директорию `drivers/`:**
   - ChromeDriver (Selenium 3): [Скачать](https://chromedriver.chromium.org/downloads)
   - GeckoDriver (для Firefox, Selenium 3): [Скачать](https://github.com/mozilla/geckodriver/releases)

5. **Запустите тесты:**

   ```bash
   pytest
   ```

## Используемые технологии

- Python
- Selenium WebDriver версии 4
- pytest

## Запуск Тестов

### Команда для Запуска

Для запуска всех тестов используйте следующую команду в терминале из корневой директории проекта:

```bash
pytest
```

