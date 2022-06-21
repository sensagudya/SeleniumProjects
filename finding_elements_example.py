from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pdb #break()

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')

#By.ID
cart = driver.find_element(By.ID, 'site-header-cart')
cart_txt = cart.text
print(cart)
print(type(cart))
print(cart_txt)

#By.ID
search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
search_field.send_keys('Hoodie')
#search_field.send_keys(Keys.ENTER)

#By.CSS_SELECTOR
#my_account = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a')
#my_account.click()

#By.XPATH
#my_account = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
#my_account.click()

#plural elements
my_products = driver.find_elements(By.CLASS_NAME, 'product')
print(my_products)

pdb.set_trace()
#driver.quit()
#driver.close(