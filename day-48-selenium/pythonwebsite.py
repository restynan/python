#https://selenium-python.readthedocs.io/locating-elements.html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_path="/Users/restynasimbwa/Development/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org/")

#find by name
driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, "q")
print(search_bar)
print(search_bar.tag_name)
print(search_bar.get_attribute('placeholder'))


#find by ID
print("\nfind by ID:**** ")
pyth = driver.find_element(By.ID, "python-network")
print(pyth.get_attribute('aria-hidden'))

#find by class
print("\nfind by class:**** ")
logo = driver.find_element(By.CLASS_NAME, "python-logo")
print(logo.size)

#find by css_selector
print("\nfind by css_selector:****")
python_doc_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget p a")
print(python_doc_link.get_attribute('innerHTML'))
print(python_doc_link.get_attribute('href'))

#find by x-PATH
print("\nfind by x-PATH:****")
submit_bug = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(submit_bug.get_attribute('innerHTML'))
print(submit_bug.get_attribute('href'))

driver.quit()
