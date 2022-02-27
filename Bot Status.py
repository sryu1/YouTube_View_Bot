# The webserver won't help that much...
from flask import Flask

views = open("Bot Status/views.txt", "r")
wsviews = views.read()
views.close()

url = open("Bot Status/url.txt", "r")
wsurl = url.read()
url.close()

viewcount = open("Bot Status/viewcount.txt", "r")
wsviewcount = viewcount.read()
viewcount.close()

# Webserver
app = Flask(__name__)


@app.route("/")
def home():
    return "Watching " + wsurl + " " + wsviewcount + " out of " + wsviews + " views." \
                                                                            " To get an updated status of the bot, " \
                                                                            "stop the webserver code and run it again"


app.run(host='0.0.0.0', port=0)
