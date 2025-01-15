from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import CONSTRUCTOR_BUNS_TAB, CONSTRUCTOR_FILLINGS_TAB, CONSTRUCTOR_SAUCES_TAB, SECTION_BUNS, SECTION_FILLINGS, SECTION_SAUCES

#Тесты для неавторизованного юзера
def test_navigate_to_sauce_section(driver, base_url):
        driver.get(f"{base_url}")
        # Нажатие на вкладку "Соусы"
        sauses_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located(CONSTRUCTOR_SAUCES_TAB))
        sauses_tab.click()
        # Проверка прокрутки до раздела "Соусы"
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(SECTION_SAUCES))

def test_navigate_to_buns_section(driver, base_url):
        driver.get(f"{base_url}")
        # Нажатие на вкладку "Соусы"
        sauses_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located(CONSTRUCTOR_SAUCES_TAB))
        sauses_tab.click()
        # Нажатие на вкладку "Булки"
        buns_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located(CONSTRUCTOR_BUNS_TAB))
        buns_tab.click()
        # Проверка прокрутки до раздела "Соусы"
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(SECTION_BUNS))

def test_navigate_to_fillings_section(driver, base_url):
        driver.get(f"{base_url}")
        # Нажатие на вкладку "Начинки"
        fillings_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located(CONSTRUCTOR_FILLINGS_TAB)) 
        fillings_tab.click()
        # Проверка прокрутки до раздела "Начинки"
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(SECTION_FILLINGS))
