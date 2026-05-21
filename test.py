from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys
import time

# Configure Headless Chrome for Jenkins
chrome_options =  Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    # 1. Target the Docker container app running on port 4000
    driver.get("http://localhost:4000")

    # 2. Find the 'Add to Cart' button and click it
    add_btn = driver.find_element(By.ID, "add-btn")
    add_btn.click()
    time.sleep(1) # Wait for page script execution

    # 3. Assert validation logic
    cart_count = driver.find_element(By.ID, "cart-count").text
    assert cart_count == "1"

    print("SUCCESS: Selenium container verification passed!")
    sys.exit(0)
except Exception as e:
    print(f"FAILURE: Automation test crashed: {e}")
    sys.exit(1)
finally:
    driver.quit()