import urllib.parse
import time
import requests
import os


def post_to_telegram(msg):
    print(msg)
    base_url = 'https://api.telegram.org/bot&text="{}'.format(msg)
    requests.get(base_url)


def check_url_inMsgList(stringToMatch, msgList):
    for i in msgList:
        if (stringToMatch in i):
            return False
    return True


try:
    f = open("oldFile.txt", "r")
    msgList = f.read().split("\n")
    f.close()
except:
    f = open("oldFile.txt", "w")
    msgList = []
    f.close()
selections = []
urr = ""
name = ""
price = ""
ourLines = 2400
url_found = 0
name_found = 0
price_found = 0
while (True):
    file1 = open('placerlog.txt', 'r')
    Lines = file1.readlines()
    file1.close()
    while (True):
        # print("-------------------------------")
        if (ourLines == len(Lines)):
            break
        elif (ourLines > len(Lines)):
            ourLines = 0
        else:
            txt = Lines[ourLines].strip()
            tlist = txt.split("&")
            ourLines = ourLines + 1
            for subtxt in tlist:
                if "eventurl=" in subtxt:
                    a = subtxt[9:len(subtxt) - 3]
                    url = "www.bet365.com/%23" + a.replace("%23", "/")
                    #url = url.replace("%23", "#")
                    for i in range(10):
                        if "F" + str(i) + "/" in url:
                            url = url.split("F" + str(i) + "/")[0] + "F" + str(i) + "/"
                    urr = url
                    url_found = 1
                elif "bet=" in subtxt:
                    name = urllib.parse.unquote(subtxt[4:len(subtxt)])
                    name_found = 1
                elif "price\":" in subtxt:
                    a = subtxt.split("price")[1]
                    price = a.split("\"")[2]
                    price = float(price)
                    price = round(price, 1)
                    price = str(price)
                    price_found = 1
                    selections.append(url + name + price)
                    msg = (url + " " + name + " " + price)
                    stringToFind = url + " " + name
                    if (check_url_inMsgList(stringToFind, msgList)):
                        post_to_telegram(msg)
                        msgList.append(msg)
                        f = open("oldFile.txt", "a+")
                        f.write(msg + "\n")
                        f.close()
                    time.sleep(0.5)
                elif "minodds=" in subtxt:
                    a = subtxt.split("minodds=")[1]
                    price = a.split("&")[0]
                    price = float(price)
                    price = round(price, 1)
                    price = str(price)
                    price_found = 1
                    selections.append(url + name + price)
                    msg = (url + " " + name + " " + price)
                    stringToFind = url + " " + name
                    if (check_url_inMsgList(stringToFind, msgList)):
                        post_to_telegram(msg)
                        msgList.append(msg)
                        f = open("oldFile.txt", "a+")
                        f.write(msg + "\n")
                        f.close()
                    time.sleep(0.5)
    time.sleep(7)
