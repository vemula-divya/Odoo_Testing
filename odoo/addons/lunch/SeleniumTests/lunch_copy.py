import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


## this code test login and navigate to fleet
def test_login_and_navigate_to_fleet(driver):
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



##this code test vechicle add functionlity
def test_vehicle_add_positive():
    driver = webdriver.Chrome()  # Initialize WebDriver (provide appropriate path to the driver)
    driver.get("http://localhost:8069/web/login")

    test_login_and_navigate_to_fleet(driver)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".o-kanban-button-new").click()
    time.sleep(3)
    driver.find_element(By.NAME, "model_id").click()

    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='o_input_dropdown']//input[@type='text']").send_keys("Aud")
    driver.find_element(By.XPATH, "//div[@class='o_input_dropdown']//input[@type='text']").send_keys(Keys.ENTER)
    time.sleep(3)

    license_plate_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "license_plate")))
    license_plate_field.send_keys("ABC123")

    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, ".o_form_button_save").click()
    time.sleep(5)
    if driver.find_element(By.CSS_SELECTOR, ".o_form_button_save").is_displayed():
        raise Exception("Test case failed")
    else:
        print("test case pass")
    driver.quit()

    # Click on the "Create" button to add a new vehicle


##this code test perform log add functionlity
def test_create_odoo_log_positive():
    driver = webdriver.Chrome()  # Initialize WebDriver (provide appropriate path to the driver)
    driver.get("http://localhost:8069/web/login")

    test_login_and_navigate_to_fleet(driver)
    menu_bar = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Fleet']")))
    menu_bar.click()

    fleet_module = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Odometers']")))
    fleet_module.click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".o_list_button_add").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".o_datepicker_input").click()

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > .day:nth-child(5)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".o_input_dropdown:nth-child(1) > .o_input").click()
    time.sleep(2)
    driver.find_element(By.ID, "ui-id-3").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".o_input_dropdown:nth-child(2) > .o_input").click()
    time.sleep(2)
    driver.find_element(By.ID, "ui-id-13").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".o_field_float").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".o_field_float").send_keys("10")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".o_list_button_save").click()
    time.sleep(5)
    if driver.find_element(By.CSS_SELECTOR, ".o_list_button_save").is_displayed():
        raise Exception("Test case failed")
    else:
        print("test case pass")

    driver.quit()


##this code search vechilce and open
def test_search_vehicle_positive():
    driver = webdriver.Chrome()  # Initialize WebDriver (provide appropriate path to the driver)
    driver.get("http://localhost:8069/web/login")
    test_login_and_navigate_to_fleet(driver)
    menu_bar = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Fleet']")))
    menu_bar.click()
    driver.find_element(By.CSS_SELECTOR, ".o_searchview_input").click()
    driver.find_element(By.CSS_SELECTOR, ".o_searchview_input").send_keys("Audi")
    driver.find_element(By.CSS_SELECTOR, ".o_searchview_input").send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        ".o_kanban_group:nth-child(1) > .oe_kanban_global_click:nth-child(2) > .o_kanban_image").click()
    # time.sleep(3)
    # if driver.find_element(By.CSS_SELECTOR, "o_view_nocontent").size!=0:
    #     raise Exception("Test case failed")
    # else:
    print("test case pass")

    driver.quit()


##this code add service and test case fails because of missing vaues
def test_service_add_negative():
    driver = webdriver.Chrome()  # Initialize WebDriver (provide appropriate path to the driver)
    driver.get("http://localhost:8069/web/login")

    test_login_and_navigate_to_fleet(driver)
    menu_bar = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Fleet']")))
    menu_bar.click()

    fleet_module = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Services']")))
    fleet_module.click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".o_list_button_add").click()

    time.sleep(2)
    driver.find_element(By.NAME, "description").send_keys("Demo")

    driver.find_element(By.CSS_SELECTOR, ".o_form_button_save").click()
    time.sleep(3)
    if driver.find_element(By.CSS_SELECTOR, ".o_form_button_save").is_displayed():
        raise Exception("Test case failed")
    else:
        print("test case pass")

    # 14 | close |  |  |
    driver.quit()
    ##this code create contrcat  and test case fails because of missing vaues


def test_contract_add_negative():
    driver = webdriver.Chrome()  # Initialize WebDriver (provide appropriate path to the driver)
    driver.get("http://localhost:8069/web/login")

    test_login_and_navigate_to_fleet(driver)
    menu_bar = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Fleet']")))
    menu_bar.click()

    fleet_module = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Contracts']")))
    fleet_module.click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".o_list_button_add").click()

    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='o_input_dropdown']//input[@type='text']").clear()

    driver.find_element(By.XPATH, "//div[@class='o_input_dropdown']//input[@type='text']").send_keys("Mit")
    driver.find_element(By.XPATH, "//div[@class='o_input_dropdown']//input[@type='text']").send_keys(Keys.ENTER)
    driver.find_element(By.CSS_SELECTOR, ".o_form_button_save").click()
    time.sleep(5)
    if driver.find_element(By.CSS_SELECTOR, ".o_form_button_save").is_displayed():
        raise Exception("Test case failed")
    else:
        print("test case pass")

    driver.quit()

