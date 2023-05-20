import time
import random
import tkinter
import customtkinter
import threading
import requests
import webbrowser as wb
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller


def main():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    app = customtkinter.CTk()
    app.geometry("800x600")
    app.title("YouTube View Bot")
    app.after(201, lambda: app.iconbitmap("Icon.ico"))

    def stream_option():
        if stream_switch.get() == 1:
            stream_switch.pack_forget()
            headless.pack_forget()
            mute.pack_forget()
            view_label.pack_forget()
            view_slider.pack_forget()
            tab_box.pack_forget()
            watchtime_box.pack_forget()
            link_box.pack_forget()
            start_button.pack_forget()
            progress.pack_forget()
            stream_switch.pack(pady=10, padx=10)
            headless.pack(pady=10, padx=10)
            mute.pack(pady=10, padx=10)
            stream_bot_label.pack(pady=10, padx=10)
            bots_watching.pack(pady=10, padx=10)
            stream_link.pack(pady=10, padx=10)
            stream_start_button.pack(pady=10, padx=10)
        else:
            stream_switch.pack_forget()
            headless.pack_forget()
            mute.pack_forget()
            stream_bot_label.pack_forget()
            bots_watching.pack_forget()
            stream_link.pack_forget()
            stream_start_button.pack_forget()
            stream_switch.pack(pady=10, padx=10)
            headless.pack(pady=10, padx=10)
            mute.pack(pady=10, padx=10)
            view_label.pack(pady=10, padx=10)
            view_slider.pack(pady=10, padx=10)
            tab_box.pack(pady=10, padx=10)
            watchtime_box.pack(pady=10, padx=10)
            link_box.pack(pady=10, padx=10)
            start_button.pack(pady=10, padx=10)
            progress.pack(pady=10, padx=10)

    def views_update(self):
        view_value = str(int(view_slider.get()))
        view_label.configure(text=f"{view_value} Views")

    def stream_bots_update(self):
        stream_bot_value = str(int(bots_watching.get()))
        stream_bot_label.configure(text=f"{stream_bot_value} Bots")

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
        current_version = "v1.3.0"
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
        stream_switch.pack_forget()
        chromedriver_autoinstaller.install()
        viewcount = 0
        drivers = []
        sites = [
            "https://search.yahoo.com/",
            "https://duckduckgo.com/",
            "https://www.google.com/",
            "https://www.bing.com/",
            "https://t.co/",
            "https://youtube.com/",
            "https://www.ecosia.org/",
            "https://www.reddit.com/",
            "https://www.twitch.tv/",
            "https://www.instagram.com/",
            "https://www.tiktok.com/",
            "https://search.brave.com",
        ]
        views = int(view_slider.get())
        number_of_drivers = int(tab_box.get())
        time_to_refresh = int(watchtime_box.get())
        url = link_box.get()

        for i in range(number_of_drivers):
            options = webdriver.ChromeOptions()
            if headless.get() == 1:
                options.add_argument("--headless")
            if mute.get() == 1:
                options.add_argument("--mute-audio")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            drivers.append(
                webdriver.Chrome(options=options, executable_path=r"chromedriver")
            )
            drivers[i].get(random.choice(sites))
            drivers[i].get(url)
            drivers[i].find_element(By.CLASS_NAME, "ytp-large-play-button").click()

        while True:
            time.sleep(time_to_refresh)
            viewcount += number_of_drivers
            progress.set(viewcount / views)

            if int(views) <= int(viewcount):
                drivers[i].quit()
                exit()
            elif int(views) > int(viewcount):
                for i in range(number_of_drivers):
                    drivers[i].refresh()

    def stream_start():
        stream_switch.pack_forget()
        chromedriver_autoinstaller.install()
        drivers = []
        sites = [
            "https://search.yahoo.com/",
            "https://duckduckgo.com/",
            "https://www.google.com/",
            "https://www.bing.com/",
            "https://t.co/",
            "https://youtube.com/",
            "https://www.ecosia.org/",
            "https://www.reddit.com/",
            "https://www.twitch.tv/",
            "https://www.instagram.com/",
            "https://www.tiktok.com/",
            "https://search.brave.com",
        ]
        number_of_bots = int(bots_watching.get())
        url = stream_link.get()
        for i in range(number_of_bots):
            options = webdriver.ChromeOptions()
            if headless.get() == 1:
                options.add_argument("--headless")
            if mute.get() == 1:
                options.add_argument("--mute-audio")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            drivers.append(
                webdriver.Chrome(options=options, executable_path=r"chromedriver")
            )
            drivers[i].get(random.choice(sites))
            drivers[i].get(url)
            drivers[i].find_element(By.CLASS_NAME, "ytp-large-play-button").click()

            def stop():
                drivers[i].quit()
                global stopped
                stopped = True

            stopped = False
            stop_button = customtkinter.CTkButton(
                master=border, command=stop, text="Stop Bot"
            )
            stop_button.pack(pady=10, padx=10)
            if stopped:
                exit()

    # Border
    border = customtkinter.CTkFrame(master=app)
    border.pack(pady=20, padx=20, fill="both", expand=True)

    # Stream Option
    stream_switch = customtkinter.CTkSwitch(
        master=border, text="Stream Mode", command=stream_option
    )
    stream_switch.pack(pady=10, padx=10)

    # Checkbox
    headless = customtkinter.CTkCheckBox(master=border, text="Headless Mode")
    headless.pack(pady=10, padx=10)
    mute = customtkinter.CTkCheckBox(master=border, text="Mute")
    mute.pack(pady=10, padx=10)
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

    # Stream Menu
    stream_bot_value = 5
    stream_bot_label = customtkinter.CTkLabel(
        master=border, justify=tkinter.LEFT, text=f"{stream_bot_value} Bots"
    )
    bots_watching = customtkinter.CTkSlider(
        master=border, from_=1, to=50, command=stream_bots_update
    )
    bots_watching.set(5)
    stream_link = customtkinter.CTkEntry(
        master=border, width=400, placeholder_text="Link"
    )
    stream_start_button = customtkinter.CTkButton(
        master=border, text="Start Bot", command=stream_start
    )

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
