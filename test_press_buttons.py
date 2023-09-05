# في ملف test_press_buttons.py

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

def test_press_buttons(setup):
    driver = setup
    try:
        # ابحث عن الزر "הסינכ" واضغط عليه
        button1 = driver.find_element(By.XPATH, "//button[contains(text(), 'הסינכ')]")
        button1.click()

        # ابحث عن الزر "המשרה |" واضغط عليه
        button2 = driver.find_element(By.XPATH, "//button[contains(text(), 'המשרה |')]")
        button2.click()

        # إضافة أي إجراءات إضافية تحتاج إلى تنفيذها بعد الضغط على الزرين.

    except Exception as e:
        driver.save_screenshot("press_buttons_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
