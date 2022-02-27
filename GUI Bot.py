import tkinter as tk
from tkinter import *
import time
import random
import os
from selenium import webdriver

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('800x600')


def views_print():
    views = views_input.get(1.0, "end-1c")
    lbl.config(text="The bot will watch the video " + views + " times")


def drivers_print():
    number_of_drivers = driver_input.get(1.0, "end-1c")
    lbl.config(text="The bot will open " + number_of_drivers + " tabs")


def url_print():
    url = url_input.get(1.0, "end-1c")
    lbl.config(text="The bot will open " + url)


def watchtime_print():
    time_to_refresh = ttr_input.get(1.0, "end-1c")
    lbl.config(text="The bot will watch for " + time_to_refresh + " seconds")


def start_bot():
    views = views_input.get(1.0, "end-1c")
    number_of_drivers = driver_input.get(1.0, "end-1c")
    url = url_input.get(1.0, "end-1c")
    time_to_refresh = ttr_input.get(1.0, "end-1c")
    viewcount = 0
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
        drivers[i].find_element_by_css_selector('[title^="Play (k)"]').click()

    for i in range(int(number_of_drivers)):
        webserver = Label(text="open Bot Status.py to see the progress of the bot")
        drivers.append(webdriver.Chrome(executable_path="chromedriver"))
        drivers[i].get(random.choice(sites))
        drivers[i].get(url)
        play_video(drivers)
        webserver.pack()
    while True:
        time.sleep(int(time_to_refresh))
        viewcount += 1
        wsviewcount()

        status = Label(text="watching video " + str(viewcount) + "out of " + str(views) + "times")
        print("viewcount: " + str(viewcount))
        status.pack()
        if int(views) <= int(viewcount):
            quit()
            Label(text="the listed amount has been viewed").pack()
            print("The listed amount of has been viewed")
            os.system("pause")
            exit()
        elif int(views) > int(viewcount):
            for i in range(int(number_of_drivers)):
                drivers[i].refresh()


view_text = Label(text="Enter the number of views")
views_input = tk.Text(frame, height=5, width=20)
view_text.pack()
views_input.pack()

# Button Creation
views_button = tk.Button(frame, text="Enter", command=views_print)
views_button.pack()

driver_text = Label(text="Enter the number of tabs you want open")
driver_input = tk.Text(frame, height=5, width=20)
driver_text.pack()
driver_input.pack()

driver_button = tk.Button(frame, text="Enter", command=drivers_print)
driver_button.pack()

url_text = Label(text="Enter the video URL")
url_input = tk.Text(frame, height=5, width=20)
url_text.pack()
url_input.pack()

url_button = tk.Button(frame, text="Enter", command=url_print)
url_button.pack()

ttr_text = Label(text="Enter the watchtime in seconds")
ttr_input = tk.Text(frame, height=5, width=20)
ttr_text.pack()
ttr_input.pack()

ttr_button = tk.Button(frame, text="Enter", command=watchtime_print)
ttr_button.pack()

tk.Button(frame, text="Start Bot", command=start_bot).pack()

lbl = tk.Label(frame, text="")
lbl.pack()
frame.mainloop()
