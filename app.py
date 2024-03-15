from flask import Flask, render_template, request
from flaskwebgui import FlaskUI
from scripts.dice import roll_dice, hit_chance
from scripts.db import db_bestiary

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def menu():
    options = ["New Game", "Load Game", "Bestiary", "Settings", "Exit Game"]
    return render_template("menu.html", options=options)


@app.route("/newgame", methods=["GET", "POST"])
def new_game():
    return render_template("error.html")


@app.route("/loadgame", methods=["GET", "POST"])
def load_game():
    return render_template("error.html")


@app.route("/bestiary", methods=["GET", "POST"])
def bestiary():
    mobs = db_bestiary()
    return render_template("bestiary.html", mobs=mobs)


@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        # User changes a setting.
        update = db_bestiary(update=True)
        return render_template("settings.html", u_bestiary=update)

    return render_template("settings.html")


@app.route("/exitgame", methods=["POST"])
def exit():
    return render_template("error.html")


if __name__ == "__main__":
    # Browser mode for debugging
    app.run(debug=True, port=5000)

    # Application using Chromium
    """FlaskUI(app=app, 
            width=800, 
            height=800, 
            browser_path="chromium/chromium.AppImage",
            server="flask").run()"""
