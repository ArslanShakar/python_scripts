# -*- coding: utf-8 -*-

import re
import random
import time

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

driver = Chrome(ChromeDriverManager().install())


# driver = Chrome('./chromedriver')


class YoutubeComments:
    file = open("youtube_comments.csv", "w")
    file.write("Comments,Url\n")

    video_urls = [
        "https://www.youtube.com/watch?v=k84QxVJd0tI&lc=Ugyp0E4icJcyTzw8CEx4AaABAg",
        "https://www.youtube.com/watch?v=k84QxVJd0tI&lc=UgyPBMHFU_govXtrYeZ4AaABAg",
    ]

    def __init__(self):
        self.get_comments()

    def get_comments(self):
        for url in self.video_urls:
            driver.get(url)
            # driver.minimize_window()
            time.sleep(4)

            time.sleep(random.choice([1, 1.5, 2, 2.5]))
            start_point = 0
            end_point = 500

            driver.execute_script(f"window.scrollTo({start_point}, {end_point});")
            time.sleep(3)

            comments = re.findall(r'ytd-comments-header-renderer">(.*)</yt-formatted-string', driver.page_source)
            highlighted = re.findall(r'style-scope ytd-badge-supported-renderer">(.*)</span>', driver.page_source)
            highlighted = [e.strip() for e in highlighted if e and e.strip()][:1]

            if "Highlighted comment" in driver.page_source:
                comments = re.findall(r'style-scope ytd-comment-renderer">(.*)</yt-formatted-string', driver.page_source)[0]
            else:
                comments = 'Not Exist'
                print(comments)
                continue
            comments = comments.replace(',', '')
            text = comments + ',' + url + "\n"
            print(text)
            self.file.write(text)
            a = 0

        driver.close()


if __name__ == "__main__":
    YoutubeComments()
