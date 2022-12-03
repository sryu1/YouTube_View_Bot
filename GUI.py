import os
import time
import random
import tkinter
import customtkinter
import json
from selenium import webdriver
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller


def config():
    if not os.path.isfile('config.json'):
        configs = {
            "Headless": headless.get(),
            "Mute": mute.get()
        }
        json_file = json.dumps(configs)
        with open("config.json", "w") as jsonfile:
            jsonfile.write(json_file)

    else:
        with open("config.json", "r") as jsonfile:
            json_options = json.load(jsonfile)
            jsonfile.close()

        def hdls():

            if json_options["Headless"] == 1:
                headless.select()
            else:
                headless.deselect()

        def sdop():

            if json_options["Mute"] == 1:
                mute.select()
            else:
                mute.deselect()

        configs = {
            "Headless": headless.get(),
            "Mute": mute.get()
        }
        json_file = json.dumps(configs)
        with open("config.json", "w") as jsonfile:
            jsonfile.write(json_file)
        hdls()
        sdop()


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("800x600")
app.title("YouTube View Bot")


def button_callback():
    print("Start Bot")


def slider_callback(value):
    print(slider_1.get())


# Border
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

# Checkbox
headless = customtkinter.CTkCheckBox(master=frame_1, text="Headless Mode", command=config)
headless.pack(pady=10, padx=10)

mute = customtkinter.CTkCheckBox(master=frame_1, text="Mute", command=config)
mute.pack(pady=10, padx=10)

# Number of views
slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
slider_1.pack(pady=10, padx=10)
slider_1.set(0.4)

# Number of tabs
entry_2 = customtkinter.CTkEntry(master=frame_1, width=200, placeholder_text="Number of tabs")
entry_2.pack(pady=10, padx=10)

# Watch time
entry_3 = customtkinter.CTkEntry(master=frame_1, width=200, placeholder_text="Watch time (seconds)")
entry_3.pack(pady=10, padx=10)

# Link
entry_4 = customtkinter.CTkEntry(master=frame_1, width=400, placeholder_text="Link")
entry_4.pack(pady=10, padx=10)

# Start Button
button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Start Bot")
button_1.pack(pady=10, padx=10)

# Bot Progress
progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=10, padx=10)
progressbar_1.set(0.0)

app.mainloop()
