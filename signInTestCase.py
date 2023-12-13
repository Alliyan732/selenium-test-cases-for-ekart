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

# Find the form elements
email_input = driver.find_element(By.ID, 'inputEmail')
password_input = driver.find_element(By.NAME, 'fpass')
signin_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'signin')))

# Fill in the form
email_input.send_keys('test@gmail.com')
password_input.send_keys('123456')

# Scroll to the element (if necessary)
driver.execute_script("arguments[0].scrollIntoView(true);", signin_button)

# Click the sign-in button using JavaScript
driver.execute_script("arguments[0].click();", signin_button)

# Wait for the page to load completely
time.sleep(2)

# Check if the page title is "Home"
if driver.title == "Home":
    print("Test case passed: Successfully logged in to the Home page")
else:
    print("Test case failed: Failed to log in to the Home page")

# Close the browser
driver.quit()
