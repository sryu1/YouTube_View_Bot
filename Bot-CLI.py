import time
import os
import random
import requests
import pysettings_manager as pysm
from selenium import webdriver
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller


def main():
    config_file = "cli_config.json"

    def config():
        if not pysm.config_file_exists(config_file):

            def hdls(headless):
                if headless == "y":
                    return True
                if headless == "n":
                    return False
                else:
                    print("Only y or n is allowed")

            headless = input("Would you like to run the bot in headless mode? (y/n): ")

            def sdop(mute):
                if mute == "y":
                    return True
                if mute == "n":
                    return False
                else:
                    print("Only y or n is allowed")

            sound = input(
                "Would you like to mute the videos while they are playing? (y/n): "
            )

            def strm(stream):
                if stream == "y":
                    return True
                if stream == "n":
                    return False
                else:
                    print("Only y or n is allowed")

            stream_mode = input("Would you like to enable stream mode for watching streams? (y/n): ")

            configs = {"Headless": str(hdls(headless)), "Mute": str(sdop(sound)), "Stream": str(strm(stream_mode))}
            pysm.save(config_file, **configs)
        else:
            config_options = input(
                "Would you like to use the previous settings for Headless mode and Sound? (y/n): "
            )
            if config_options == "y":
                pass
            else:

                def hdls(headless):
                    if headless == "y":
                        return True
                    if headless == "n":
                        return False
                    else:
                        print("Only y or n is allowed")

                headless = input("Would you like to run the bot in headless mode? (y/n): ")

                def sdop(mute):
                    if mute == "y":
                        return True
                    if mute == "n":
                        return False
                    else:
                        print("Only y or n is allowed")

                sound = input(
                    "Would you like to mute the videos while they are playing? (y/n): "
                )

                def strm(stream):
                    if stream == "y":
                        return True
                    if stream == "n":
                        return False
                    else:
                        print("Only y or n is allowed")

                stream_mode = input("Would you like to enable stream mode for watching streams? (y/n): ")

                configs = {"Headless": str(hdls(headless)), "Mute": str(sdop(sound)), "Stream": str(strm(stream_mode))}
                pysm.save(config_file, **configs)

    def update():
        ghrapi = requests.get(
            "https://api.github.com/repos/sryu1/YouTube_View_Bot/releases/latest"
        )
        current_version = "1.2.3"
        latest_version = str(ghrapi.json()["name"])
        if current_version < latest_version:
            print(
                f"A new update ({latest_version}) has been released!\n"
                f"Get the release at https://github.com/sryu1/YouTube_View_Bot/releases/tag/{latest_version}\n"
                f"Check the changelogs to see if there are any updates to the CLI, "
                f"updates will most likely be for the GUI"
            )

    update()
    config()
    chromedriver_autoinstaller.install()
    viewcount = 0
    views = input("how many views would you like: ")
    number_of_drivers = int(input("Enter the number of tabs you want open: "))
    time_to_refresh = int(input("Choose your watch time (seconds): "))
    url = input("Enter Video URL: ")
    drivers = []
    sites = [
        "https://search.yahoo.com/",
        "https://duckduckgo.com/",
        "https://www.google.com/",
        "https://www.bing.com/",
        "https://t.co/",
        "https://youtube.com",
    ]

    wsviews = open("Bot Status/views.txt", "w")
    wsurl = open("Bot Status/url.txt", "w")
    wsviews.write(views)
    wsviews.close()
    wsurl.write(url)
    wsurl.close()
    json_options = pysm.load(config_file)

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
        if json_options["Mute"] == 0:
            pass
        else:
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

        print("view count = " + str(viewcount))
        if int(views) <= int(viewcount):
            drivers[i].quit()
            print("the listed amount has been viewed")
            os.system("pause")
            exit()
        elif int(views) > int(viewcount):
            for i in range(number_of_drivers):
                drivers[i].refresh()


if __name__ == "__main__":
    main()
