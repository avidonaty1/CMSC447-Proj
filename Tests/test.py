import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_email_and_click(browser):
    # Step 1: Visit your local website
    browser.get("http://localhost:5173/")

    time.sleep(2)  # Wait for page to load

    # Step 2: Find the email input
    email_input = browser.find_element(By.NAME, "email")
    email_input.click()
    email_input.send_keys("umbc")

    time.sleep(1)

    # Step 3: Find the Login button
    login_button = browser.find_element(By.XPATH, '//button[contains(text(), "Login")]')

    # Step 4: Click the Login button
    login_button.click()

    time.sleep(2)

    # (Optional) Step 5: Verify that login was successful
    # You could check if the page URL changes, or some new element appears
    # Example:
    # assert "dashboard" in browser.current_url

