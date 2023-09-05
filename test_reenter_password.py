# في ملف test_reenter_password.py

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

def test_reenter_password(setup):
    driver = setup
    try:
        # إعادة إدخال كلمة المرور مرة أخرى
        reenter_password_input = driver.find_element(By.ID, "reenter_password_input")
        reenter_password_input.send_keys("Password123")  # يمكنك تغيير هذا إلى كلمة المرور الخاصة بك

        # إضافة أي إجراءات إضافية تحتاج إلى تنفيذها بعد إعادة إدخال كلمة المرور.

    except Exception as e:
        driver.save_screenshot("reenter_password_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
