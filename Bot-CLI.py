import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller


def main():
    def config():
        def hdls(headless):
            if headless == "y":
                return 1
            if headless == "n":
                return 0
            else:
                raise Exception("Only y or n is allowed")

        headless = input("Would you like to run the bot in headless mode? (y/n): ")

        def sdop(mute):
            if mute == "y":
                return 1
            if mute == "n":
                return 0
            else:
                raise Exception("Only y or n is allowed")

        sound = input(
            "Would you like to mute the videos while they are playing? (y/n): "
        )

        def strm(stream):
            if stream == "y":
                return 1
            if stream == "n":
                return 0
            else:
                raise Exception("Only y or n is allowed")

        stream_mode = input(
            "Would you like to enable stream mode for watching streams? (y/n): "
        )

        configs = {
            "Headless": hdls(headless),
            "Mute": sdop(sound),
            "Stream": strm(stream_mode),
        }
        return configs

    def update():
        ghrapi = requests.get(
            "https://api.github.com/repos/sryu1/YouTube_View_Bot/releases/latest"
        )
        current_version = "v1.2.8"
        latest_version = str(ghrapi.json()["name"])
        if current_version < latest_version:
            print(
                f"A new update ({latest_version}) has been released!\n"
                f"Get the release at https://github.com/sryu1/YouTube_View_Bot/releases/tag/{latest_version}"
            )

    update()
    configs = config()
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

    def play_video(drivers):
        drivers[i].find_element(By.CLASS_NAME, "ytp-large-play-button").click()

    if configs["Stream"] != 1:
        viewcount = 0
        views = input("how many views would you like: ")
        number_of_drivers = int(input("Enter the number of tabs you want open: "))
        time_to_refresh = int(input("Choose your watch time (seconds): "))
        url = input("Enter Video URL: ")

        for i in range(number_of_drivers):
            options = webdriver.ChromeOptions()
            if configs["Headless"] == 1:
                options.add_argument("--headless")
            if configs["Mute"] == 1:
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

            print("view count = " + str(viewcount))
            if int(views) <= int(viewcount):
                drivers[i].quit()
                input("The listed amount has been viewed \nPress Enter to exit . . .")
                exit()
            elif int(views) > int(viewcount):
                for i in range(number_of_drivers):
                    drivers[i].refresh()
    elif configs["Stream"]:
        number_of_drivers = int(
            input("Enter the number of bots you would like watching the stream: ")
        )
        url = input("Enter Video URL: ")

        for i in range(number_of_drivers):
            options = webdriver.ChromeOptions()
            if configs["Headless"] == 1:
                options.add_argument("--headless")
            if configs["Mute"] == 0:
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


if __name__ == "__main__":
    main()
