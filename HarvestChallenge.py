import os
import sys
from flask import Flask, render_template, redirect, url_for, request
from Infrastructure.ChampionManager import get_champions
from Infrastructure.ChampionManager import add_champion
from Models.Champion import Champion

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_folder)
else:
    app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    championsDB = get_champions()
    return render_template("index.html", championsDB=championsDB)


@app.route('/add_champion_stats', methods=["POST"])
def add_champion_stats():
    champion_name = request.form.get("champion-name")
    champion_matches = request.form.get("champion-matches")
    champion_souls = request.form.get("champion-souls")
    champion_stats = request.form.get("champion-stats")
    champion_game_time = request.form.get("champion-game-time")
    champion = Champion(name=champion_name, matches=champion_matches,
                        souls=champion_souls, stats=champion_stats, game_time=champion_game_time)
    add_champion(new_champion=champion)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
