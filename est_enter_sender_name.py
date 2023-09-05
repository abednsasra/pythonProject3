# في ملف test_enter_sender_name.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import utils.config

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL)

    yield driver
    driver.quit()

def test_enter_sender_name(setup):
    driver = setup
    try:
        # إدخال اسم المرسل
        sender_name_input = driver.find_element(By.ID, "sender_name_input")
        sender_name_input.send_keys("John Smith")  # يمكنك تغيير هذا إلى الاسم الذي تحتاجه

        # إضافة أي إجراءات إضافية تحتاج إلى تنفيذها بعد إدخال اسم المرسل.

    except Exception as e:
        driver.save_screenshot("enter_sender_name_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
