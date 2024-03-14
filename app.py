from flask import Flask, render_template
from flaskwebgui import FlaskUI
from scripts.dice import roll_dice, hit_chance
from scripts.dnd_api import monsters, fetch_beast
from scripts.db import update_bestiary

app = Flask(__name__, static_url_path="/static")
app.config.from_object(__name__)


@app.route("/")
def menu():
    options = ["New Game", "Load Game", "Bestiary", "Settings", "Exit Game"]
    return render_template("menu.html", options=options)


@app.route("/newgame", methods=["POST"])
def new_game():
    return render_template("error.html")


@app.route("/loadgame", methods=["POST"])
def load_game():
    return render_template("error.html")


@app.route("/bestiary", methods=["POST", "GET"])
def bestiary():
    mobs = monsters()
    mob_data = [fetch_beast(i) for i in mobs]
    return render_template("bestiary.html", mobs=mobs)


@app.route("/settings", methods=["POST"])
def settings():
    update = update_bestiary
    return render_template("settings.html", u_bestiary=update)


@app.route("/exitgame", methods=["POST"])
def exit():
    return render_template("error.html")


if __name__ == "__main__":
    # Browser mode for debugging
    app.run(debug=True, port=50000)

    # Application using Chromium
    """FlaskUI(app=app, 
            width=800, 
            height=800, 
            browser_path="chromium/chromium.AppImage",
            server="flask").run()"""
