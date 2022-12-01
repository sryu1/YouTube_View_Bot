import json


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

with open("config.json", "r") as jsonfile:
    options = json.load(jsonfile)
    jsonfile.close()

if options["Headless"] == "True":
    print("Headless is true")
