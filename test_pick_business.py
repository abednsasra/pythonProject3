# في ملف test_pick_business.py

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

def test_pick_business(setup):
    driver = setup
    try:
        # ابحث عن عنصر يمثل نوع العمل الذي ترغب في اختياره
        # يمكنك استخدام Selenium للبحث عن هذا العنصر والنقر عليه.
        # مثال:
        # business_option = driver.find_element(By.XPATH, "//label[contains(text(), 'Restaurant')]")
        # business_option.click()

        # بعد النقر على الخيار المطلوب، قم بتأكيد الاختيار
        # يمكنك القيام بذلك بالتحقق من وجود عنصر تأكيد على الشاشة.
        # مثال:
        # confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Confirm')]")
        # assert confirm_button.is_displayed()

    except Exception as e:
        driver.save_screenshot("pick_business_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
