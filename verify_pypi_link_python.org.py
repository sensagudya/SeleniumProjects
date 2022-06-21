from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.python.org/')

cur_title = driver.title
expected_title = 'Welcome to Python.org'

if cur_title != expected_title:
    raise Exception('Went to python.org but got the wrong title. Current title: {}'.format(cur_title))

pypi_header_link_locator = '#top > nav > ul > li.pypi-meta > a'
pypi_header_link_element = driver.find_element(By.CSS_SELECTOR, pypi_header_link_locator)
pypi_header_link_element.click()

cur_url = driver.current_url
expected_url = 'https://pypi.org/'
assert cur_url == expected_url, f'Clicked on pypi, but the url opened was: {cur_url}'
print('PASS')

#driver.quit()