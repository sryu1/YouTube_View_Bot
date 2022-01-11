from flask import Flask

views = open("views.txt", "r")
wsviews = views.read()
views.close()

url = open("url.txt", "r")
wsurl = url.read()
url.close()

viewcount = open("viewcount.txt", "r")
wsviewcount = viewcount.read()
viewcount.close()

# Webserver
app = Flask(__name__)


@app.route("/")
def home():
    return "Watched " + wsurl + " " + wsviewcount + " out of " + wsviews + " views."


app.run(host='0.0.0.0', port=8080)
