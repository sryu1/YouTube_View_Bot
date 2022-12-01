import time
import os
import random
import json
from selenium import webdriver
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller


def config():
    if not os.path.isfile('config.json'):
        def hdls(headless):
            if headless == "y":
                return True
            if headless == "n":
                return False

        headless = input("Would you like to run the bot in headless mode? (y/n): ")
        print(hdls(headless))

        def sdop(mute):
            if mute == "y":
                return True
            if mute == "n":
                return False

        sound = input("Would you like to mute the videos while they are playing? (y/n): ")
        print(sdop(sound))
        configs = {
            "Headless": str(hdls(headless)),
            "Mute": str(sdop(sound))
        }
        json_file = json.dumps(configs)
        with open("config.json", "w") as jsonfile:
            jsonfile.write(json_file)
    else:
        config_options = input("Would you like to use the previous settings for Headless mode and Sound? (y/n): ")
        if config_options == "y":
            pass
        else:
            def hdls(headless):
                if headless == "y":
                    return True
                if headless == "n":
                    return False

            headless = input("Would you like to run the bot in headless mode? (y/n): ")
            print(hdls(headless))

            def sdop(mute):
                if mute == "y":
                    return True
                if mute == "n":
                    return False

            sound = input("Would you like to mute the videos while they are playing? (y/n): ")
            print(sdop(sound))
            configs = {
                "Headless": str(hdls(headless)),
                "Mute": str(sdop(sound))
            }
            json_file = json.dumps(configs)
            with open("config.json", "w") as jsonfile:
                jsonfile.write(json_file)


config()
