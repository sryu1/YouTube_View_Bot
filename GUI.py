import os
import time
import random
import tkinter
import customtkinter
import json
from selenium import webdriver
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller


def main():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.geometry("800x600")
    app.title("YouTube View Bot")

    drivers = []
    sites = ['https://search.yahoo.com/', 'https://duckduckgo.com/', 'https://www.google.com/',
             'https://www.bing.com/', 'https://t.co/', 'https://youtube.com']

    def config():
        if not os.path.isfile('config.json'):
            configs = {
                "Headless": headless.get(),
                "Mute": mute.get()
            }
            json_file = json.dumps(configs)
            with open("config.json", "w") as jsonfile:
                jsonfile.write(json_file)

    with open("config.json", "r") as jsonfile:
        json_options = json.load(jsonfile)
        jsonfile.close()

    def write_settings():
        configs = {
            "Headless": headless.get(),
            "Mute": mute.get()
        }
        json_file = json.dumps(configs)
        with open("config.json", "w") as jsonfile:
            jsonfile.write(json_file)

    def slider_callback(value):
        global views
        views = int(view_slider.get())

    def start_bot():
        write_settings()
        chromedriver_autoinstaller.install()
        viewcount = 0
        print(views)
        number_of_drivers = tab_box.get()
        print(number_of_drivers)
        time_to_refresh = watchtime_box.get()
        print(time_to_refresh)
        url = link_box.get()
        print(url)
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
            options = webdriver.ChromeOptions()
            if json_options["Headless"] == 1:
                options.add_argument("--headless")
            if json_options["Mute"] == 1:
                pass
            else:
                options.add_argument("--mute-audio")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            drivers.append(webdriver.Chrome(options=options,
                                            executable_path=r"chromedriver"))
            drivers[i].get(random.choice(sites))
            drivers[i].get(url)
            play_video(drivers)

        while True:
            time.sleep(time_to_refresh)
            viewcount += 1
            wsviewcount()

            print("view count = " + str(viewcount))
            if int(views) <= int(viewcount):
                drivers[i].quit()
                print("the listed amount has been viewed")
                os.system("pause")
                exit()
            elif int(views) > int(viewcount):
                for i in range(number_of_drivers):
                    drivers[i].refresh()

    # Border

    border = customtkinter.CTkFrame(master=app)
    border.pack(pady=20, padx=20, fill="both", expand=True)

    # Checkbox
    headless = customtkinter.CTkCheckBox(master=border, text="Headless Mode", command=config)
    headless.pack(pady=10, padx=10)
    if json_options["Headless"] == 1:
        headless.select()
    else:
        headless.deselect()

    mute = customtkinter.CTkCheckBox(master=border, text="Mute", command=config)
    mute.pack(pady=10, padx=10)
    if json_options["Mute"] == 1:
        mute.select()
    else:
        mute.deselect()

    # Number of views
    view_number = customtkinter.CTkLabel(master=border, justify=tkinter.LEFT, text="Number")
    view_number.pack(pady=10, padx=10)
    view_slider = customtkinter.CTkSlider(master=border, command=slider_callback, from_=1, to=50)
    view_slider.pack(pady=10, padx=10)
    view_slider.set(20)

    # Number of tabs
    tab_box = customtkinter.CTkEntry(master=border, width=200, placeholder_text="Number of tabs")
    tab_box.pack(pady=10, padx=10)

    # Watch time
    watchtime_box = customtkinter.CTkEntry(master=border, width=200, placeholder_text="Watch time (seconds)")
    watchtime_box.pack(pady=10, padx=10)

    # Link
    link_box = customtkinter.CTkEntry(master=border, width=400, placeholder_text="Link")
    link_box.pack(pady=10, padx=10)
    # Bot Progress
    progress = customtkinter.CTkProgressBar(master=border)
    progress.set(0.0)
    # Start Button
    button_1 = customtkinter.CTkButton(master=border, command=start_bot, text="Start Bot")
    button_1.pack(pady=10, padx=10)

    progress.pack(pady=10, padx=10)
    app.mainloop()


if __name__ == "__main__":
    main()
