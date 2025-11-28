import time
from selenium.webdriver.common.by import By
from tests.selenium.base import get_driver

BASE_URL = "http://localhost:3000"


def test_dashboard_charts():
    driver = get_driver()
    driver.get(f"{BASE_URL}/dashboard")

    time.sleep(2)

    # Check chart elements
    chart = driver.find_element(By.ID, "prediction-history-chart")
    assert chart is not None

    # Check stats card exists
    stats_card = driver.find_element(By.ID, "stats-card")
    assert stats_card is not None

    driver.quit()
