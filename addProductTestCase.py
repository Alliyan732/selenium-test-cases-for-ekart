import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set up the Selenium driver with a Service object
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.maximize_window()

# Load the sign-in page
driver.get('http://127.0.0.1:8000/adminLogin')  # Replace with the actual URL of the sign-in page

# Find the form elements
email_input = driver.find_element(By.ID, 'inputEmail')
password_input = driver.find_element(By.NAME, 'fpass')
signin_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'signin')))

# Fill in the form
email_input.send_keys('alliyan732@gmail.com')
password_input.send_keys('123456')

# Scroll to the element (if necessary)
driver.execute_script("arguments[0].scrollIntoView(true);", signin_button)

# Click the sign-in button using JavaScript
driver.execute_script("arguments[0].click();", signin_button)

# Wait for the page to load completely
time.sleep(2)

# Check if the page title is "Home"
if driver.title == "Admin Dashboard":
    print("Successfully logged in to the Admin Dashboard")
else:
    print("Failed to log in to the Admin Panel")

# click products from the side bar
products = driver.find_element(By.XPATH, '/html/body/div/aside/div[2]/nav/ul/li[2]/a')
products.click()
time.sleep(2)

if driver.title == "Admin Dashboard":
    print("Successfully redirected to products page")
else:
    print("Failed to redirect to products page")

# add new item button
add_products = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div[1]/a/button')
add_products.click()
time.sleep(2)

if driver.title == "Admin Dashboard":
    print("Successfully redirected Add Products Page")
else:
    print("Failed to redirect to Add products page")

# add name
name = add_image = driver.find_element(By.XPATH, '//*[@id="name"]')
name.send_keys("Product_Name")

# short desc
name = add_image = driver.find_element(By.XPATH, '//*[@id="short_desc"]')
name.send_keys("short desc")

# add image
add_image = driver.find_element(By.XPATH, '//*[@id="image"]')
file_path = 'E:\Projects\My projects\Ekart semister project\images\c_t-shirt_men.png'
add_image.send_keys(file_path)

# add category
category = add_image = driver.find_element(By.XPATH, '//*[@id="category"]')
category.send_keys("New Collection")

# description
description = add_image = driver.find_element(By.XPATH, '//*[@id="desc"]')
description.send_keys("description")

# keyword
keyword = add_image = driver.find_element(By.XPATH, '//*[@id="keywords"]')
keyword.send_keys("keyword")

# price
price = add_image = driver.find_element(By.XPATH, '//*[@id="price"]')
price.send_keys(5900)

# submit btn
submit = driver.find_element(By.XPATH, '//*[@id="payment-button"]')
submit.click()
time.sleep(2)

if driver.title == "Admin Dashboard":
    print("Successfully added new product")
else:
    print("Failed to add new product")

time.sleep(5)

# Close the browser
driver.quit()
