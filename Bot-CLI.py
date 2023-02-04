import time
import os
import random
import requests
import pysettings_manager as pysm
from selenium import webdriver
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller


def main():
    user = os.getlogin()
    config_file = os.path.join(
        "C:",
        os.sep,
        "Users",
        user,
        "Documents",
        "YouTube View Bot",
        "cli_config.json",
    )
    ytvb_data = str("C:/" + "Users/" + user + "/" + "Documents/" + "YouTube View Bot/")
    if (
        os.path.exists(
            os.path.join(
                os.path.join(
                    "C:",
                    os.sep,
                    "Users",
                    user,
                    "Documents",
                    "YouTube View Bot",
                    "Bot Status",
                )
            )
        )
        is False
    ):
        os.mkdir(ytvb_data + "Bot Status/")
        wsviews = open(
            ytvb_data + "Bot Status/" + "views.txt",
            "w+",
        )
        wsurl = open(
            ytvb_data + "Bot Status/" + "url.txt",
            "w+",
        )
        wsvc = open(
            ytvb_data + "Bot Status/" + "viewcount.txt",
            "w+",
        )
        wsviews.close()
        wsurl.close()
        wsvc.close()

    def config():
        if not pysm.config_file_exists(config_file):

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
                "Headless": str(hdls(headless)),
                "Mute": str(sdop(sound)),
                "Stream": str(strm(stream_mode)),
            }
            pysm.save(config_file, **configs)
        else:
            try:
                if pysm.load(config_file)["Headless"] != "None":
                    if pysm.load(config_file)["Mute"] != "None":
                        if pysm.load(config_file)["Stream"] != "None":
                            config_options = input(
                                "Would you like to use the previous settings for Stream mode, Headless mode and Sound? (y/n): "
                            )
            except TypeError:
                config_options = None
            if config_options != "y" or config_options is None:

                def hdls(headless):
                    if headless == "y":
                        return 1
                    if headless == "n":
                        return 0
                    else:
                        raise Exception("Only y or n is allowed")

                headless = input(
                    "Would you like to run the bot in headless mode? (y/n): "
                )

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
                    "Headless": str(hdls(headless)),
                    "Mute": str(sdop(sound)),
                    "Stream": str(strm(stream_mode)),
                }
                pysm.save(config_file, **configs)

    def update():
        ghrapi = requests.get(
            "https://api.github.com/repos/sryu1/YouTube_View_Bot/releases/latest"
        )
        current_version = "v1.2.7"
        latest_version = str(ghrapi.json()["name"])
        if current_version < latest_version:
            print(
                f"A new update ({latest_version}) has been released!\n"
                f"Get the release at https://github.com/sryu1/YouTube_View_Bot/releases/tag/{latest_version}"
            )

    update()
    config()
    chromedriver_autoinstaller.install()

    drivers = []
    sites = [
        "https://search.yahoo.com/",
        "https://duckduckgo.com/",
        "https://www.google.com/",
        "https://www.bing.com/",
        "https://t.co/",
        "https://youtube.com",
    ]

    json_options = pysm.load(config_file)

    def wsviewcount():
        wsvc = open(ytvb_data + "Bot Status/viewcount.txt", "w")
        wsvc.write(str(viewcount))
        wsvc.close()

    def play_video(drivers):
        ActionChains(drivers[i]).send_keys("k").perform()

    if json_options["Stream"] != 1:
        viewcount = 0
        views = input("how many views would you like: ")
        number_of_drivers = int(input("Enter the number of tabs you want open: "))
        time_to_refresh = int(input("Choose your watch time (seconds): "))
        url = input("Enter Video URL: ")

        wsviews = open(ytvb_data + "Bot Status/views.txt", "w")
        wsurl = open(ytvb_data + "Bot Status/url.txt", "w")
        wsviews.write(views)
        wsviews.close()
        wsurl.write(url)
        wsurl.close()

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
    elif json_options["Stream"]:
        number_of_drivers = int(
            input("Enter the number of bots you would like watching the stream: ")
        )
        url = input("Enter Video URL: ")
        wsurl = open(ytvb_data + "Bot Status/url.txt", "w")
        wsurl.write(url)
        wsurl.close()

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


if __name__ == "__main__":
    main()
