from flask import Flask, render_template
from flaskwebgui import FlaskUI
from scripts.dice import roll_dice, hit_chance

app = Flask(__name__, static_url_path="/static")
app.config.from_object(__name__)


@app.route("/")
def menu():
    """
    Player starts here.
    """
    options = ["New Game", "Load Game", "Demo", "Settings", "Exit Game"]
    return render_template("menu.html", options=options)


@app.route("/NewGame", methods=["POST"])
def new_game():
    """
    Starts a new game.
    """
    return render_template("error.html")


@app.route("/LoadGame", methods=["POST"])
def load_game():
    return render_template("error.html")


@app.route("/Demo", methods=["POST"])
def demo():
    return render_template("error.html")


@app.route("/Settings", methods=["POST"])
def settings():
    return render_template("error.html")


@app.route("/ExitGame", methods=["POST"])
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
