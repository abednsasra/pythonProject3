# في ملف test_enter_buyme_website.py

import pytest
from selenium import webdriver
from utils.config import Config

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

def test_enter_buyme_website(setup):
    driver = setup
    try:
        # قم بإضافة الأكواد اللازمة لزيارة موقع BuyMe
        # يمكنك استخدام Selenium للانتقال إلى URL الموقع الإلكتروني المطلوب.
        # مثال:
        # driver.get("https://buyme.co.il/")

        # قم بإضافة أي إجراءات إضافية تحتاج إلى تنفيذها على هذا الموقع.

    except Exception as e:
        driver.save_screenshot("enter_buyme_website_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
