from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException
#import time

def open_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver

def go_to_homepage(driver):
    driver.get('http://demostore.supersqa.com/')

def add_first_item_to_cart(driver):
    first_add_button = driver.find_element(By.CLASS_NAME, 'add_to_cart_button')
    first_add_button.click()

def go_to_cart_page(driver):
    driver.get('http://demostore.supersqa.com/cart')

def apply_coupon(driver, coupon_code):
    coupon_field = driver.find_element(By.ID, 'coupon_code')
    coupon_field.send_keys(coupon_code)
    apply_btn = driver.find_element(By.CSS_SELECTOR, '#post-7 > div > div > form > table > tbody > tr:nth-child(2) > td > div > button')
    apply_btn.click()

#def verify_cart_has_item(driver): #keep refreshing
#    for i in range(5):
#        try:
#            driver.find_element(By.CLASS_NAME, 'cart_item')
#            return
#        except NoSuchElementException:
#            print('Item not in cart. Retrying after 2 secs.')
#            time.sleep(2)
#            driver.refresh()

def get_displayed_error_message(driver):
    return driver.find_element(By.XPATH, '//*[@id="post-7"]/div/div/div[1]/ul/li').text

if __name__ == '__main__':
    driver = open_browser()
    go_to_homepage(driver)
    add_first_item_to_cart(driver)
    go_to_cart_page(driver)
    #verify_cart_has_item(driver)
    apply_coupon(driver, 'fakeone')
    get_displayed_error_message(driver)
    err_msg = get_displayed_error_message(driver)
    exp_msg = 'Coupon "fakeone" does not exist!'
    assert err_msg == exp_msg, f'Unexpected error message:{err_msg}'
    print('PASS')
    #driver.quit()