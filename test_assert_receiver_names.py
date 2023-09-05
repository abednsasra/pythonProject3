# في ملف test_assert_receiver_names.py

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


def test_assert_receiver_names(setup):
    driver = setup
    try:
        # إلزام الاختبار بانتظار حتى تظهر الأسماء في الصفحة (يمكن استبدال المعرفات بالمعرفات الفعلية)
        receiver_names_elements = driver.find_elements(By.XPATH, "//div[@class='receiver-name']")

        # قائمة بالأسماء المتوقعة للمستلمين (يمكن تغييرها وتكييفها وفقًا لمتطلبات المشروع)
        expected_receiver_names = ["مستلم 1", "مستلم 2", "مستلم 3"]

        # التحقق من أن عدد الأسماء على الصفحة يتطابق مع العدد المتوقع
        assert len(receiver_names_elements) == len(expected_receiver_names)

        # التحقق من أن الأسماء المعروضة على الصفحة تتطابق مع الأسماء المتوقعة
        for index, receiver_element in enumerate(receiver_names_elements):
            assert receiver_element.text.strip() == expected_receiver_names[index]

    except Exception as e:
        driver.save_screenshot("assert_receiver_names_error.png")
        pytest.fail(f"An exception occurred: {str(e)}")
