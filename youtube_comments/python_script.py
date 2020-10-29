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
        "https://www.youtube.com/watch?v=hxADTEJalRw&lc=Ugzd-7JseYg2D9Id_g14AaABAg",
        "https://www.youtube.com/watch?v=hxADTEJalRw&lc=UgyPL40tI4JXMFXJNZ94AaABAg",
        "https://www.youtube.com/watch?v=hxADTEJalRw&lc=UgxCYHuK7ny2J10VJ5x4AaABAg",
        "https://www.youtube.com/watch?v=hxADTEJalRw&lc=Ugx--fYkxjD9RmazXtN4AaABAg",
        "https://www.youtube.com/watch?v=hxADTEJalRw&lc=UgzLLaMknj7Jtv5w8wp4AaABAg",
        "https://www.youtube.com/watch?v=hxADTEJalRw&lc=Ugy1Bazfdgf4q9PcKHx4AaABAg",
        "https://www.youtube.com/watch?v=hxADTEJalRw&lc=Ugy1BazdfgdfggdgKHx4AaABAg",
        "https://www.youtube.com/watch?v=hxADTEJalRw&lc=Ugdfgdf-J_94q9PcKHx4AaABAg",
        "https://www.youtube.com/watch?v=hxADTEJalRw&lc=UgwTLVv6Y452e4Bspid4AaABAg",
        "https://www.youtube.com/watch?v=hxADTEJalRw&lc=Ugy1Baz-J_94q9PcKHx4AaABAg",
    ]

    def __init__(self):
        self.get_comments()

    def get_comments(self):
        for url in self.video_urls:
            try:
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
                    comment = \
                        re.findall(r'style-scope ytd-comment-renderer">(.*)</yt-formatted-string', driver.page_source)[
                            0]
                else:
                    comment = 'Not Exist'
                    print(comment)
                    continue
                if not comment.strip():
                    comment = "unreadable comment / symbol"
                comment = comment.replace(',', '')
                text = comment + ',' + url + "\n"
                print(text)
                self.file.write(text)
            except Exception as e:
                print("Error in url: " + url)
                print(e)
        driver.close()


if __name__ == "__main__":
    YoutubeComments()
