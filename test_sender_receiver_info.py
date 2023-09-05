# في ملف test_sender_receiver_info.py

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

def test_sender_receiver_info(setup):
    driver = setup
    try:
        # ملء معلومات المرسل
        sender_name_input = driver.find_element(By.ID, "sender_name")
        sender_name_input.send_keys("John Doe")

        # ملء معلومات المستلم
        receiver_name_input = driver.find_element(By.ID, "receiver_name")
        receiver_name_input.send_keys("Jane Smith")

        event_dropdown = driver.find_element(By.ID, "event_dropdown")
        event_dropdown.click()

        # اختر نوع الحدث (على سبيل المثال، عيد ميلاد)
        birthday_option = driver.find_element(By.XPATH, "//option[contains(text(), 'Birthday')]")
        birthday_option.click()

        blessing_input = driver.find_element(By.ID, "blessing")
        blessing_input.send_keys("Happy Birthday!")

        # رفع صورة
        upload_button = driver.find_element(By.ID, "upload_button")
        upload_button.click()

        # إنتقال إلى الخطوة التالية (على سبيل المثال، الذهاب إلى BuyMe website)
        next_button = driver.find_element(By.ID, "next_button")
        next_button.click()

        # قم بإضافة المزيد من الأكواد للتحقق من تأكيد الانتقال

    except Exception as e:
        driver.save_screenshot("sender_receiver_info_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
