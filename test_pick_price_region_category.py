# في ملف test_pick_price_region_category.py

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

def test_pick_price_region_category(setup):
    driver = setup
    try:
        # اختيار نقطة السعر
        price_point_dropdown = driver.find_element(By.ID, "price_point_dropdown")
        price_point_dropdown.click()
        # اختيار نقطة السعر المطلوبة (على سبيل المثال: "100-200")
        price_option = driver.find_element(By.XPATH, "//option[contains(text(), '100-200')]")
        price_option.click()

        # اختيار المنطقة
        region_dropdown = driver.find_element(By.ID, "region_dropdown")
        region_dropdown.click()
        # اختيار المنطقة المطلوبة (على سبيل المثال: "Tel Aviv")
        region_option = driver.find_element(By.XPATH, "//option[contains(text(), 'Tel Aviv')]")
        region_option.click()

        # اختيار الفئة
        category_dropdown = driver.find_element(By.ID, "category_dropdown")
        category_dropdown.click()
        # اختيار الفئة المطلوبة (على سبيل المثال: "Gift Cards")
        category_option = driver.find_element(By.XPATH, "//option[contains(text(), 'Gift Cards')]")
        category_option.click()

        # إضافة أي إجراءات إضافية تحتاج إلى تنفيذها بعد اختيار العناصر المطلوبة.

    except Exception as e:
        driver.save_screenshot("pick_price_region_category_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
