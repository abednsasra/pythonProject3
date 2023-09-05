# في ملف test_home_screen.py

import pytest
from selenium import webdriver
from utils.config import Config

BASE_URL = "https:\\buyme.co.il\\"


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL)
    BASE_URL="https:\\buyme.co.il\\"
    yield driver
    driver.quit()


def test_home_screen(setup):
    driver = setup
    try:
    # قم بإضافة الأكواد اللازمة للتحقق من وجود عنصر معين على الشاشة الرئيسية
    # يمكنك استخدام Selenium للبحث عن العناصر والتحقق من وجودها.

    # مثال:
   # home_page_title = driver.find_element(By.XPATH, "//h1[contains(text(), 'Welcome to BuyMe')]")
    # assert home_page_title.is_displayed()

    except Exception as e:
        driver.save_screenshot("home_screen_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
