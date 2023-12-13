import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set up the Selenium driver with a Service object
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.maximize_window()

# Load the sign-in page
driver.get('http://127.0.0.1:8000/Ekart/login')  # Replace with the actual URL of the sign-in page


# Wait for the element to become clickable
register_now_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'registerNow')))


# Scroll to the element (if necessary)
driver.execute_script("arguments[0].scrollIntoView(true);", register_now_link)

# Click the sign-in button using JavaScript
driver.execute_script("arguments[0].click();", register_now_link)
time.sleep(5) 

name = driver.find_element(By.NAME , 'rName')
email = driver.find_element(By.NAME , 'rEmail')
password = driver.find_element(By.NAME , 'rPass')
conferm_password = driver.find_element(By.NAME , 'rcPass')
country = driver.find_element(By.NAME , 'country')
age = driver.find_element(By.NAME , 'age')


name.send_keys('test')
email.send_keys('testregister1@gmail.com')
password.send_keys('123456')
conferm_password.send_keys('123456')
country.send_keys('Pakistan')
age.send_keys(20)

register_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btnRegister')))

# Scroll to the element (if necessary)
driver.execute_script("arguments[0].scrollIntoView(true);", register_btn)

# Click the sign-in button using JavaScript
driver.execute_script("arguments[0].click();", register_btn)

# Check if the page title is "Home"
if driver.title == "Ekart Login":
    print("Test case passed: Successfully Registered and redirected to login page")
else:
    print("Test case failed: Unable to register!")


driver.quit()