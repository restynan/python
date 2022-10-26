from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path="/Users/restynasimbwa/Development/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

#clicking on a-link
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
article_count.click()
#print(article_count.get_attribute('innerHTML'))
#driver.quit()

#find by link  text
hurricane_julia = driver.find_element(By.LINK_TEXT, "Hurricane Julia")
hurricane_julia.click()

#add text to input tag

search = driver.find_element(By.NAME, "search")
search.send_keys("John")
search.send_keys(Keys.ENTER)

driver.quit()
