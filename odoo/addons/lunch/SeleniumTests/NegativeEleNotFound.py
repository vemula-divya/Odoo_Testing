import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the webdriver (assuming you have already installed it)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome()

# Navigate to the Odoo login page
driver.get("http://localhost:8069/web/login/")
time.sleep(10)

# Login
username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
username.send_keys("divyavemula1227@gmail.com")
password = driver.find_element(By.NAME,"password" )
password.send_keys("Odoo_151")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Verify successful login
WebDriverWait(driver, 10).until(EC.title_contains("Discuss"))
assert "Odoo" in driver.title
menu_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dropdown-toggle  ")))
menu_bar.click()

lunch_module = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'o_app') and contains(text(), 'Lunch')]")))
lunch_module.click()
time.sleep(3)
if driver.title == "Odoo - Order Your Lunch":
        time.sleep(3)
        print("Lunch loaded successfully")

# Order a Pizza Margherita sandwich
driver.get("http://localhost:8069/web#cids=1&menu_id=119&action=199&model=lunch.product&view_type=kanban")
time.sleep(10)

pizza = driver.find_element(By.XPATH, "//*[contains(text(),'Tomatoes, cuba')]")
pizza.click()

add_to_cart = driver.find_element(By.XPATH, "//*[contains(text(),'Add To Cart')]")
add_to_cart.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Order now')]")))
