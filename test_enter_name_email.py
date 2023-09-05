# في ملف test_enter_name_email.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

def test_enter_name_email(setup):
    driver = setup
    try:
        # إدخال الاسم الأول
        first_name_input = driver.find_element(By.ID, "first_name")
        first_name_input.send_keys("John")

        # إدخال عنوان بريد إلكتروني صالح
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys("john@example.com")

        # إضافة أي إجراءات إضافية تحتاج إلى تنفيذها بعد إدخال البيانات.

    except Exception as e:
        driver.save_screenshot("enter_name_email_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
