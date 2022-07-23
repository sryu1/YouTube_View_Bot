import time
import os
import random
from selenium import webdriver
from selenium.webdriver import ActionChains

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
viewcount = 0
views = input("how many views would you like: ")
number_of_drivers = int(input("Enter the number of tabs you want open: "))
time_to_refresh = int(input("Choose your watch time (seconds): "))
url = input("Enter Video URL: ")
drivers = []
sites = ['https://search.yahoo.com/', 'https://duckduckgo.com/', 'https://www.google.com/',
         'https://www.bing.com/', 'https://t.co/', 'https://youtube.com']

wsviews = open("Bot Status/views.txt", 'w')
wsurl = open("Bot Status/url.txt", 'w')
wsviews.write(views)
wsviews.close()
wsurl.write(url)
wsurl.close()


def wsviewcount():
    wsvc = open("Bot Status/viewcount.txt", 'w')
    wsvc.write(str(viewcount))
    wsvc.close()


def play_video(drivers):
    ActionChains(drivers[i]) \
        .send_keys("k") \
        .perform()


for i in range(number_of_drivers):
    print("open Bot Status.py to see the progress of the bot")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    drivers.append(webdriver.Chrome(options=options, executable_path=r"chromedriver"))
    drivers[i].get(random.choice(sites))
    drivers[i].get(url)
    play_video(drivers)

while True:
    time.sleep(time_to_refresh)
    viewcount += 1
    wsviewcount()

    print("viewcount= " + str(viewcount))
    if int(views) <= int(viewcount):
        quit()
        print("the listed amount has been viewed")
        os.system("pause")
        exit()
    elif int(views) > int(viewcount):
        for i in range(number_of_drivers):
            drivers[i].refresh()
