from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

LOGIN_URL = "http://localhost:8069/web/login/"
LUNCH_URL = "http://localhost:8069/web#cids=1&menu_id=119&action=199&model=lunch.product&view_type=kanban"
CHROMEDRIVER_PATH = "/opt/odoo15/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")
browser = webdriver.Chrome()

def my_login_test_case():
    browser.get(LOGIN_URL)
    assert "Odoo" in browser.title
    username_input = browser.find_element(By.NAME, "login")
    username_input.clear()
    username_input.send_keys("divyavemula1227@gmail.com")
    password_input = browser.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys("Odoo_151")
    password_input.send_keys(Keys.RETURN)
    time.sleep(3)
    assert "Odoo" in browser.title

def order_pizza_margherita_sandwich_test_case():
    browser.get(LUNCH_URL)
    time.sleep(10)
    pizza_margherita = browser.find_element(By.XPATH, "//*[contains(text(),'Tomatoes, Mozzarella')]")
    pizza_margherita.click()
    time.sleep(4)
    add_to_cart_button = browser.find_element(By.XPATH, "//*[contains(text(),'Add To Cart')]")
    add_to_cart_button.click()
    time.sleep(5)
    order_now_button = browser.find_element(By.XPATH, "//*[contains(text(),'Order now')]")
    order_now_button.click()
    time.sleep(4)
    assert "6.90€" in browser.page_source

my_login_test_case()
order_pizza_margherita_sandwich_test_case()
browser.close()
