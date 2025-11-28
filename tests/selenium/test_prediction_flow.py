import time
from selenium.webdriver.common.by import By
from tests.selenium.base import get_driver

BASE_URL = "http://localhost:3000"


def test_prediction_flow():
    driver = get_driver()
    driver.get(f"{BASE_URL}/predict")

    # Fill fields
    driver.find_element(By.ID, "loan_amount").send_keys("25000")
    driver.find_element(By.ID, "income").send_keys("75000")
    driver.find_element(By.ID, "age").send_keys("32")
    driver.find_element(By.ID, "employment_length").send_keys("5")
    driver.find_element(By.ID, "credit_score").send_keys("720")
    driver.find_element(By.ID, "dti").send_keys("12")

    purpose_dropdown = driver.find_element(By.ID, "loan_purpose")
    purpose_dropdown.send_keys("debt_consolidation")

    # Submit prediction
    driver.find_element(By.ID, "predict-btn").click()

    time.sleep(3)

    # Check result exists
    result = driver.find_element(By.ID, "prediction-result")
    assert result is not None
    assert "Prediction:" in result.text

    driver.quit()
