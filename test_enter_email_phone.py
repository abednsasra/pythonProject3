# في ملف test_enter_email_phone.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import config

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

def test_enter_email_phone(setup):
    driver = setup
    try:
        # إدخال عنوان البريد الإلكتروني أو رقم الهاتف
        email_phone_input = driver.find_element(By.ID, "email_phone_input")
        email_phone_input.send_keys("john@example.com")  # يمكنك تغيير هذا إلى العنوان أو الرقم الذي تحتاجه

        # إضافة أي إجراءات إضافية تحتاج إلى تنفيذها بعد إدخال العنوان أو الرقم.

    except Exception as e:
        driver.save_screenshot("enter_email_phone_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
