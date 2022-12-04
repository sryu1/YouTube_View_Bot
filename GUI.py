import os
import time
import random
import tkinter
import customtkinter
import json
from selenium import webdriver
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("800x600")
app.title("YouTube View Bot")


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
    views = int(view_slider.get())
    print(views)


def start_bot():
    write_settings()


# Border
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

# Checkbox
headless = customtkinter.CTkCheckBox(master=frame_1, text="Headless Mode", command=config)
headless.pack(pady=10, padx=10)
if json_options["Headless"] == 1:
    headless.select()
else:
    headless.deselect()

mute = customtkinter.CTkCheckBox(master=frame_1, text="Mute", command=config)
mute.pack(pady=10, padx=10)
if json_options["Mute"] == 1:
    mute.select()
else:
    mute.deselect()

# Number of views
view_number = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Number")
view_number.pack(pady=10, padx=10)
view_slider = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=1, to=50)
view_slider.pack(pady=10, padx=10)
view_slider.set(20)

# Number of tabs
tab_box = customtkinter.CTkEntry(master=frame_1, width=200, placeholder_text="Number of tabs")
tab_box.pack(pady=10, padx=10)

# Watch time
watchtime_box = customtkinter.CTkEntry(master=frame_1, width=200, placeholder_text="Watch time (seconds)")
watchtime_box.pack(pady=10, padx=10)

# Link
link_box = customtkinter.CTkEntry(master=frame_1, width=400, placeholder_text="Link")
link_box.pack(pady=10, padx=10)

# Start Button
button_1 = customtkinter.CTkButton(master=frame_1, command=start_bot, text="Start Bot")
button_1.pack(pady=10, padx=10)

# Bot Progress
progress = customtkinter.CTkProgressBar(master=frame_1)
progress.pack(pady=10, padx=10)
progress.set(0.0)

app.mainloop()
