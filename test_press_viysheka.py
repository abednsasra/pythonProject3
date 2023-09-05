# في ملف test_press_viysheka.py

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

def test_press_viysheka(setup):
    driver = setup
    try:
        # ابحث عن الزر 'וישכע' واضغط عليه
        button_viysheka = driver.find_element(By.XPATH, "//button[contains(text(), 'וישכע')]")
        button_viysheka.click()

        # إضافة أي إجراءات إضافية تحتاج إلى تنفيذها بعد الضغط على الزر.

    except Exception as e:
        driver.save_screenshot("press_viysheka_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
