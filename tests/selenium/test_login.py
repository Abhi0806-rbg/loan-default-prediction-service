import time
from selenium.webdriver.common.by import By
from tests.selenium.base import get_driver

BASE_URL = "http://localhost:3000"   # frontend URL


def test_login_flow():
    driver = get_driver()
    driver.get(f"{BASE_URL}/login")

    time.sleep(1)

    # Email
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("test@example.com")

    # Password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("password123")

    # Click Login
    login_btn = driver.find_element(By.ID, "login-btn")
    login_btn.click()

    time.sleep(2)

    # Assertion: redirected to dashboard
    assert "dashboard" in driver.current_url

    driver.quit()
