# في ملف test_pick_email_sms.py

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

def test_pick_email_sms(setup):
    driver = setup
    try:
        # اختيار وسيلة الاتصال المفضلة (بريد إلكتروني أو رسالة نصية)
        email_option = driver.find_element(By.ID, "email_option")
        email_option.click()  # اختيار البريد الإلكتروني

        # أو
        # sms_option = driver.find_element(By.ID, "sms_option")
        # sms_option.click()  # اختيار رسالة نصية

        # إضافة أي إجراءات إضافية تحتاج إلى تنفيذها بعد اختيار الوسيلة المفضلة.

    except Exception as e:
        driver.save_screenshot("pick_email_sms_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
