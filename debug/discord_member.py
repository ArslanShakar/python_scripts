import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import csv
import math
from time import sleep
import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost.com",
#     user="amine",
#     password="password",
#     database="tui"
# )

# ennter email password here for discord:

email = "belkapis@gmail.com"
pass_word = "fatiha06$"

email = "huwaiguest@gmail.com"
pass_word = "huwaiguest786"

path = None  # "C://Users//itzka//AppData//Local//Google//Chrome//User Data//Profile 5"
join_url = "https://discord.gg/WBgWqnkc"
# options room
join_url = "https://discord.gg/sfQUJ58phv"

snrtrades = "https://discord.gg/XF29hDgh"
traderead = "https://discord.gg/RQT89m5N"

davinci = "https://discord.com/channels/747156249874923580/763461288520056853"

join_url = traderead
servername = 'traderead'

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

if path != None:
    chrome_options.add_argument('--user-data-dir={p}'.format(p=path))
data = []


def accept_invite(driver, url):
    if url == None:
        pass
    else:
        driver.get(url)
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div/div/section/div/button'))
            )
            driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/section/div/button').click()
        except TimeoutException as t:
            print(t)
            driver.quit()


def copyit(driver, xpath):
    driver.find_element_by_xpath('//*[@id="user-context-devmode-copy-id"]/div').click()


def save_to_csv():
    with open('users.csv', 'w+', newline='', encoding='utf-8') as listI:
        writer = csv.writer(listI)
        writer.writerow(["ID", "Username"])
        writer.writerows(data)


def login(driver):
    if pass_word == None:
        print("Please Fill Username & Password Variable")
        return False
    else:
        driver.get("https://discord.com/login")
        try:
            user_box = driver.find_element_by_xpath(
                '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input').send_keys(
                email)
            pass_box = driver.find_element_by_xpath(
                '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input').send_keys(
                pass_word)
            driver.find_element_by_xpath(
                '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]').click()
            time.sleep(5)
        except TimeoutException as t:
            print("Can't Logged In. More Information :", t)
            driver.quit()


def check_for_homepage(driver):
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="private-channels-0"]/div/div[2]/div/div'))
    )


# def insertToMysql(servername, userid, username, rolecolor):
#     mycursor = mydb.cursor()
#     print(servername, userid, username, rolecolor)
#     sql = "INSERT IGNORE INTO disinviter (servername, userid,username,rolecolor) VALUES (%s, %s, %s, %s)"
#     print(sql)
#
#     val = (servername, userid, username, rolecolor)
#
#     mycursor.execute(sql, val)
#
#     mydb.commit()
#     print(mycursor.rowcount, "record inserted.")


def runTheScroll(chrome, i, totalRounds):
    actionChains = ActionChains(chrome)
    sleep(2)
    print("Batch #" + str(i) + " out of a totalround of " + str(totalRounds))
    listI = chrome.find_elements_by_class_name('member-3-YXUe')
    print("total members: " + str(len(listI)))
    totalItemsProcessed = 0
    i_d = 1
    color = "-_-"
    actionChains = ActionChains(chrome)
    for memberItem in listI:
        try:
            currentCat = chrome.find_elements_by_class_name('member-3-YXUe')[totalItemsProcessed]
            # get id works :
            actionChains.context_click(memberItem).perform()
            chrome.find_element_by_xpath('//*[@id="user-context-devmode-copy-id"]/div').click()
            i_d = pyperclip.paste()
            username = memberItem.text

            # actionChains.move_to_element(memberItem).context_click(currentCat).perform()
            # chrome.find_element_by_xpath('//*[@id="user-context-devmode-copy-id"]/div').click()
            chrome.execute_script("arguments[0].scrollIntoView();", memberItem)

            # color  =  currentCat.find_elements_by_class_name("'[class^=roleColor-]'").value_of_css_property('color')
            # color  =  currentCat.findElement(By.xpath(".//div[starts-with(@class,'roleColor-')]"));
            # this works
            # color  =memberItem.get_attribute("data-list-item-id")

            # color = memberItem.find_element_by_xpath("//span[starts-with(@class, 'roleColor-')]").get_attribute("style")

            # color = currentCat.find_element_by_xpath("//span[starts-with(@class, 'roleColor-')]").get_attribute("style")
            # color = currentCat.find_elements_by_css_selector("span").get_attribute("style")
            color = memberItem.find_element_by_xpath(
                "//span[contains(@style,'color: rgb(241, 196, 15)')]").get_attribute("style")

            color = color.replace("color: ", "")
            color = color.replace(";", "")

            print(color)
            # color+
            print(str(i_d) + " : " + username + " => " + " ###" + str(totalItemsProcessed))

            # insertToMysql(servername, str(i_d), username, color )

            # chrome.execute_script("arguments[0].scrollIntoView();", i)

            totalItemsProcessed += 1

            print("items processed: " + str(totalItemsProcessed))
            sleep(3)

            # len(listI)
            # use 10
            if totalItemsProcessed > 12:
                # save_to_csv()
                # totalItemsProcessed = 0
                # chrome.execute_script("document.querySelector('.members-1998pB').scrollTo(0, 600 * "+str(i)+")" )

                # sleep(5)
                # listI = chrome.find_elements_by_class_name('member-3-YXUe')
                sleep(1)
            if i >= totalRounds:
                break

        except (StaleElementReferenceException, NoSuchElementException) as e:
            print(e)


def right_click(chrome):
    try:
        WebDriverWait(chrome, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'member-3-YXUe'))
        )

        membersid = '[aria-label="Members"]'
        runthis = "document.querySelector('" + membersid + "').querySelector('[class^=content-]').offsetHeight"
        totalHeightSidebar = chrome.execute_script("return " + runthis)
        numberOfScrolls = math.ceil(totalHeightSidebar / 720)
        # sleep(2)
        # PROCESS EACH BATCH THEN SCROLL
        i = 1
        # while i <= numberOfScrolls:

        while i <= numberOfScrolls:
            runTheScroll(chrome, i, numberOfScrolls)
            i += 1
        chrome.quit()

        # f = chrome.find_elements_by_class_name('member-3-YXUe')

        # document.querySelector(".members-1998pB").scrollTo(0, document.querySelector(".members-1998pB").scrollHeight * 3111)
        # document.querySelector(".members-1998pB").scrollTo(0, 600 * 5)
        ##document.querySelector('[aria-label="Members"]').scrollTo(0,1000)
        # document.querySelector('[aria-label="Members"]').clientHeight or .height
        # document.querySelector('[aria-label="Members"]').querySelector('[class^=content-]').height`
        # GET TOTAL HEIGHT AND CALCULATE HOW MANY SCROLLS TO DO

        # left_height = chrome.find_element_by_xpath('//*[@aria-label="Members"]/div').get_window_size()
        # left_height = driver.find_element_by_id('members-').get_window_size()
        # left_height = chrome.find_element_by_xpath("//*[starts-with(@id, 'members-')").get_window_size()
        # left_height = chrome.find_elements_by_xpath("//*[starts-with(@id, 'members-')]")

        # document.querySelectorAll('.member-3-YXUe')[15].innerText

        # indexD = 0
        # for i in f:
        #     try:
        #         actionChains.move_to_element(i).context_click(i).perform()
        #         chrome.find_element_by_xpath('//*[@id="user-context-devmode-copy-id"]/div').click()

        #         username = i.text
        #         i_d = pyperclip.paste()
        #         # print(i.text)
        #         # print(i_d)
        #         data.append([str(i_d), str(username)])
        #         #previousHeight = await page.evaluate('document.body.scrollHeight');
        #         #chrome.execute_script("arguments[0].scrollIntoView();", i)
        #         chrome.execute_script("arguments[0].scrollTo(0, 200 )", i)
        #         indexD+=1
        #         sleep(2)
        #     except (StaleElementReferenceException, NoSuchElementException) as e:
        #         print(e)
        # save_to_csv()
        # chrome.quit()

    except (StaleElementReferenceException, NoSuchElementException) as n:
        print("More Info :", n)


chrome = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

login(chrome)
check_for_homepage(chrome)
accept_invite(chrome, join_url)
right_click(chrome)
