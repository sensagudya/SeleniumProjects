from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.python.org/')
driver.implicitly_wait(10)

cur_title = driver.title
expected_title = 'Welcome to Python.org'

if cur_title != expected_title:
    raise Exception('Went to python.org but got the wrong title. Current title: {}'.format(cur_title))

search_field_id = 'id-search-field'
search_field_element = driver.find_element(By.ID, search_field_id)
search_field_element.send_keys('testing')

go_btn_id = 'submit'
go_bt_element = driver.find_element(By.ID, go_btn_id)
go_bt_element.click()

first_result_xpath = '//*[@id="content"]/div/section/form/ul/li[1]'
first_result_element = driver.find_element(By.XPATH, first_result_xpath)

import pdb; pdb.set_trace()

#assert first_result_element.is_displayed(), f'After searching the result is not displayed.'
if first_result_element.is_displayed():
    print('PASS')
else:
    raise Exception(f'After searching the result is not displayed.')

driver.quit()