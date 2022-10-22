from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path="/Users/restynasimbwa/Development/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Josephine")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Catherine")

email_address = driver.find_element(By.NAME, "email")
email_address.send_keys("catherinej@gmail.com")

sign_up = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up.click()
driver.quit()