import time

from selenium.webdriver import Chrome, Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver

# username = "ekolboio@gmail.com"
# password = "sQJyLRyV!/6!V89"
username = "huwaiguest@gmail.com"
password = "arslan_amazon"

driver = Chrome(ChromeDriverManager().install())
# driver = Firefox(GeckoDriverManager().install())
# options = webdriver.FirefoxOptions()
# options.add_argument("no-sandbox")
# options.add_argument("--allow-insecure-localhost")
# options.add_argument("--disable-gpu")
# options.add_argument('--ignore-certificate-errors')
# options.set_headless()
# capabilities = options.to_capabilities()
# driver = webdriver.Firefox(executable_path="./geckodriver", options=options, desired_capabilities=capabilities)


driver.get("https://www.amazon.com")
time.sleep(5)

login_url = driver.find_element_by_css_selector('a.a-button-text').get_attribute('href')
driver.get(login_url)
time.sleep(5)

email_txt_field = driver.find_element_by_css_selector('.a-input-text.a-span12')
time.sleep(0.2)
email_txt_field.click()
email_txt_field.send_keys(username)

continue_btn = driver.find_element_by_css_selector('.a-button-input')
continue_btn.click()
time.sleep(5)

password_txt_field = driver.find_element_by_css_selector('.a-input-text.a-span12')
time.sleep(0.2)
password_txt_field.send_keys(password)

submit_btn = driver.find_element_by_id('signInSubmit')
time.sleep(1)
submit_btn.click()
time.sleep(7)

if 'Type characters' in driver.page_source:
    password_txt_field.send_keys(password)

time.sleep(24 * 60)
a = 0
