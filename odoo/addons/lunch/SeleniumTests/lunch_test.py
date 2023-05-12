import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the webdriver (assuming you have already installed it)
driver = webdriver.Chrome()

# Navigate to the Odoo login page
driver.get("http://localhost:8069/web/login")
  # Replace "your_odoo_url" with the actual URL
time.sleep(10)

# Login
username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "login")))  # Replace "login" with the actual login input field ID
username.send_keys("divyavemula1227@gmail.com")  # Replace "your_username" with the actual username
password = driver.find_element(By.NAME,"password" )  # Replace "password" with the actual password input field ID
password.send_keys("Odoo_151")  # Replace "your_password" with the actual password
login_button = driver.find_element(By.CSS_SELECTOR,
                                       "button[type='submit']")  # Replace with actual login button selector
login_button.click()

  # Verify successful login
WebDriverWait(driver, 10).until(EC.title_contains("Discuss"))  # Wait for the page to load
assert "Odoo" in driver.title
menu_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dropdown-toggle  ")))
menu_bar.click()

lunch_module = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'o_app') and contains(text(), 'Lunch')]")))
lunch_module.click()
time.sleep(3)
if driver.title == "Odoo - Order Your Lunch":
        time.sleep(3)
        print("Lunch loaded succefully")