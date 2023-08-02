import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager

# Установка опций для Firefox
options = Options()
options.headless = True

# Создание веб-драйвера Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

# Увеличение значения timeout до 30 секунд
wait = WebDriverWait(driver, 30)

# URL страницы для скрапинга
url = "https://luding.ru/collection/wine/"

try:
    # Открытие страницы
    driver.get(url)
    
    # Ожидание загрузки элементов на странице
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item")))
    
    # Получение информации о продуктах
    products = driver.find_elements(By.CSS_SELECTOR, ".product-item")
    
    for product in products:
        print(product.text)
    
except TimeoutException as e:
    print(f"Превышено время ожидания: {e}")
except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрытие веб-драйвера
    driver.quit()

