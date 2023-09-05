# في ملف test_logged_in.py

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


def test_logged_in(setup):
    driver = setup
    try:
    # قم بتنفيذ تسجيل الدخول هنا
    # يمكنك البحث عن العناصر المطلوبة وملء بيانات تسجيل الدخول (اسم المستخدم وكلمة المرور).

    # مثال:
    # username_input = driver.find_element(By.ID, "username")
    # username_input.send_keys("your_username")
    # password_input = driver.find_element(By.ID, "password")
    # password_input.send_keys("your_password")
    # login_button = driver.find_element(By.ID, "login_button")
    # login_button.click()

    # بعد تسجيل الدخول، قم بإضافة الإجراءات المطلوبة على الموقع.
    # مثال:
    # قم بالبحث عن العناصر والأزرار التي تحتاج إلى التفاعل معها ونفذ الإجراءات الضرورية.

    except Exception as e:
        driver.save_screenshot("logged_in_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
