import os
import sys
from flask import Flask, render_template, redirect, url_for, request
from Infrastructure.ChampionManager import get_champions
from Infrastructure.ChampionManager import add_champion
from Infrastructure.ChampionManager import edit_champion
from Infrastructure.ChampionManager import delete_champion
from Models.Champion import Champion
from Infrastructure.FilesOperations import read_data_from_file
from Infrastructure.FilesOperations import save_data_to_file



def get_champion_web_model():
    champion_id = request.form.get("champion-id")
    champion_name = request.form.get("champion-name")
    champion_matches = request.form.get("champion-matches")
    champion_souls = request.form.get("champion-souls")
    champion_stats = request.form.get("champion-stats")
    champion_game_time = request.form.get("champion-game-time")
    champion = Champion(id=champion_id,name=champion_name, matches=champion_matches,
                        souls=champion_souls, stats=champion_stats, game_time=champion_game_time)
    return champion


if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_folder)
else:
    app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    read_data_from_file()
    championsDB = get_champions()
    return render_template("index.html", championsDB=championsDB)


@app.route('/add_champion_stats', methods=["POST"])
def add_champion_stats():
    champion = get_champion_web_model()
    add_champion(new_champion=champion)
    save_data_to_file()
    return redirect(url_for("index"))


@app.route('/edit_champ', methods=["POST"])
def edit_champ_stats():
    champion = get_champion_web_model()
    edit_champion(champion)
    save_data_to_file()
    return redirect(url_for("index"))


@app.route('/delete_champ', methods=["POST"])
def delete_champ_stats():
    champion_id = request.form.get("champion-id")
    delete_champion(champion_id)
    save_data_to_file()
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run() #debug=True
