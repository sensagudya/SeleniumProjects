from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.get('http://demostore.supersqa.com/')
print(driver.title)