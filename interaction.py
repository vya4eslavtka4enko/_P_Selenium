from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

element = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

el = element.text
print(el)
# print(el.split(' ')[0])

driver.quit()