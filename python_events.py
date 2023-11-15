from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org')
dic = {}
time_element = driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
for time in time_element:
    # print(time.text)
    ...
event_element = driver.find_elements(By.CSS_SELECTOR,'.event-widget li a')
for event in event_element:
    # print(event.text)
    ...
for i in range(len(time_element)):
    dic[i] = {
        "time":time_element[i].text,
        'event':event_element[i].text
    }
print(dic)
driver.quit()