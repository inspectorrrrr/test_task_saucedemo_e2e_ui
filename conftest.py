import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture
def driver():
    # Используем Chrome, но можно заменить на Firefox, используя соответствующие драйверы.
    # Для Chrome:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Для Firefox (раскомментируй, если хочешь использовать Firefox):
    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.maximize_window()
    yield driver
    driver.quit()
