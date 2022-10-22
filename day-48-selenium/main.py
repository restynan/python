#https://selenium-python.readthedocs.io/locating-elements.html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_path="/Users/restynasimbwa/Development/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org/")

#create  a dictionay  containing up coming events
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget li time")
# for time in event_times:
#     print(time.get_attribute('datetime').split('T')[0])

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# for name in event_names:
#     print(name.get_attribute('innerHTML'))

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].get_attribute('datetime').split('T')[0],
        "name": event_names[n].get_attribute('innerHTML'),
    }

print(events)




'''
driver.get("https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=asc_df_B06Y1MP2PY/?tag=hyprod-20&linkCode=df0&hvadid=198091976077&hvpos=&hvnetw=g&hvrand=821977292336599848&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9053228&hvtargid=pla-349697940639&psc=1")
price = driver.find_element(By.CLASS_NAME, "a-offscreen")
print(price)
print(price.get_attribute('innerHTML'))

driver.quit()
'''