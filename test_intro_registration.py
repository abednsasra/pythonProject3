#  test_intro_registration.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.config import Config

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

def test_intro_registration(setup):
    driver = setup
    try:
        # بدء الاختبار هنا
        intro_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]")
        intro_button.click()

        # انتظار حتى يظهر زر التسجيل
        wait = WebDriverWait(driver, 10)
        registration_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Register')]"))
        )
        registration_button.click()


        first_name_input = driver.find_element(By.ID, "first_name")
        first_name_input.send_keys("John")

        last_name_input = driver.find_element(By.ID, "last_name")
        last_name_input.send_keys("Doe")

        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys("johndoe@example.com")

        # اكتب المزيد من الإجراءات هنا

        # انتظار بضع ثواني ثم قم بالتحقق من تأكيد التسجيل
        confirmation_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Registration successful.')]"))
        )

        # التحقق من أن الرسالة تأكيد التسجيل تظهر بشكل صحيح
        assert confirmation_message.text == "Registration successful."

    except Exception as e:
        # التقاط لقطة شاشة عند حدوث استثناء
        driver.save_screenshot("intro_registration_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
