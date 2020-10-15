# -*- coding: utf-8 -*-

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

username = "ekolboio@gmail.com"
password = "sQJyLRyV!/6!V89"

# username = "huwaiguest@gmail.com"
# password = "arslan_amazon"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
action = ActionChains(driver)
time.sleep(1)

# driver.get('http://www.amazon.in')
driver.get('http://www.amazon.com')
time.sleep(3)

firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[1]')
action.move_to_element(firstLevelMenu).perform()
time.sleep(3)

secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
secondLevelMenu.click()
time.sleep(3)

signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')
signinelement.send_keys(username)
time.sleep(3)

cont = driver.find_element_by_xpath('//*[@id="continue"]')
cont.click()
time.sleep(3)

passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
passwordelement.send_keys(password)
time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
time.sleep(60 * 1)
