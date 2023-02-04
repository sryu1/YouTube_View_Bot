import os
import time
import random
import tkinter
import customtkinter
import threading
import requests
import pysettings_manager as pysm
import webbrowser as wb
from selenium import webdriver
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller


def main():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    app = customtkinter.CTk()
    app.geometry("800x600")
    app.title("YouTube View Bot")
    app.after(201, lambda: app.iconbitmap("Icon.ico"))
    config_file = os.path.join(
        "C:",
        os.sep,
        "Users",
        os.getlogin(),
        "Documents",
        "YouTube View Bot",
        "config.json",
    )

    if not pysm.config_file_exists(config_file):
        configs = {"Headless": 0, "Mute": 0}
        pysm.save(config_file, **configs)

    json_options = pysm.load(config_file)

    def write_settings():
        configs = {"Headless": headless.get(), "Mute": mute.get()}
        pysm.save(config_file, **configs)

    def progress_bar():
        viewcount = open("Bot Status/viewcount.txt", "r")
        wsviewcount = int(viewcount.read())
        viewcount.close()
        views = int(view_slider.get())
        progress.set(wsviewcount / views)

    def views_update(self):
        view_value = str(int(view_slider.get()))
        view_label.configure(text=f"{view_value} Views")

        # Updates

    def update():
        def open_updates():
            wb.open(
                f"https://github.com/sryu1/YouTube_View_Bot/releases/tag/{latest_version}"
            )
            update_window.destroy()

        def destroy_update_window():
            update_window.destroy()

        ghrapi = requests.get(
            "https://api.github.com/repos/sryu1/YouTube_View_Bot/releases/latest"
        )
        current_version = "v1.2.6"
        latest_version = str(ghrapi.json()["name"])
        if current_version < latest_version:
            update_window = customtkinter.CTkToplevel()
            update_window.geometry("300x120")
            update_window.title("Update")

            # create label on CTkToplevel window
            update_label = customtkinter.CTkLabel(
                update_window,
                text=f"A new update ({latest_version}) has been released!",
            )
            update_close_button = customtkinter.CTkButton(
                master=update_window, command=destroy_update_window, text="Close"
            )
            update_button = customtkinter.CTkButton(
                master=update_window, command=open_updates, text="Update"
            )
            update_label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
            update_button.pack()
            update_close_button.pack()

    def start_bot():
        write_settings()
        chromedriver_autoinstaller.install()
        viewcount = 0
        drivers = []
        sites = [
            "https://search.yahoo.com/",
            "https://duckduckgo.com/",
            "https://www.google.com/",
            "https://www.bing.com/",
            "https://t.co/",
            "https://youtube.com",
        ]
        views = int(view_slider.get())
        number_of_drivers = int(tab_box.get())
        time_to_refresh = int(watchtime_box.get())
        url = link_box.get()
        wsviews = open("Bot Status/views.txt", "w")
        wsurl = open("Bot Status/url.txt", "w")
        wsviews.write(str(views))
        wsviews.close()
        wsurl.write(url)
        wsurl.close()

        def wsviewcount():
            wsvc = open("Bot Status/viewcount.txt", "w")
            wsvc.write(str(viewcount))
            wsvc.close()

        def play_video(drivers):
            ActionChains(drivers[i]).send_keys("k").perform()

        for i in range(number_of_drivers):
            options = webdriver.ChromeOptions()
            if json_options["Headless"] == 1:
                options.add_argument("--headless")
            if json_options["Mute"] == 1:
                options.add_argument("--mute-audio")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            drivers.append(
                webdriver.Chrome(options=options, executable_path=r"chromedriver")
            )
            drivers[i].get(random.choice(sites))
            drivers[i].get(url)
            play_video(drivers)

        while True:
            time.sleep(time_to_refresh)
            viewcount += number_of_drivers
            wsviewcount()
            progress_bar()

            if int(views) <= int(viewcount):
                drivers[i].quit()
            elif int(views) > int(viewcount):
                for i in range(number_of_drivers):
                    drivers[i].refresh()

    # Border
    border = customtkinter.CTkFrame(master=app)
    border.pack(pady=20, padx=20, fill="both", expand=True)

    # Checkbox
    headless = customtkinter.CTkCheckBox(master=border, text="Headless Mode")
    headless.pack(pady=10, padx=10)
    if json_options["Headless"] == 1:
        headless.select()
    else:
        headless.deselect()

    mute = customtkinter.CTkCheckBox(master=border, text="Mute")
    mute.pack(pady=10, padx=10)
    if json_options["Mute"] == 1:
        mute.select()
    else:
        mute.deselect()
    # Bot Progress
    progress = customtkinter.CTkProgressBar(master=border)
    progress.set(0.0)

    # Number of views
    view_value = 20
    view_label = customtkinter.CTkLabel(
        master=border, justify=tkinter.LEFT, text=f"{view_value} Views"
    )
    view_slider = customtkinter.CTkSlider(
        master=border, from_=1, to=50, command=views_update
    )
    view_label.pack(pady=10, padx=10)
    view_slider.pack(pady=10, padx=10)
    view_slider.set(20)

    # Number of tabs
    tab_box = customtkinter.CTkEntry(
        master=border, width=200, placeholder_text="Number of tabs"
    )
    tab_box.pack(pady=10, padx=10)

    # Watch time
    watchtime_box = customtkinter.CTkEntry(
        master=border, width=200, placeholder_text="Watch time (seconds)"
    )
    watchtime_box.pack(pady=10, padx=10)

    # Link
    link_box = customtkinter.CTkEntry(master=border, width=400, placeholder_text="Link")
    link_box.pack(pady=10, padx=10)

    # Start Button
    start_button = customtkinter.CTkButton(
        master=border,
        command=threading.Thread(target=start_bot).start,
        text="Start Bot",
    )
    start_button.pack(pady=10, padx=10)

    progress.pack(pady=10, padx=10)

    update()

    app.mainloop()


if __name__ == "__main__":
    main()
