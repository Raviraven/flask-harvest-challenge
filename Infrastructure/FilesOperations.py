from Models.Champion import parse_dictionary_to_champion
from Infrastructure.ChampionManager import add_champion
from Infrastructure.ChampionManager import get_champions
from Infrastructure.ChampionManager import clear_champions_list
import json

filename = "HarvestChallenge.txt"


def read_data_from_file():
    try:
        f = open(filename, "r")
        clear_champions_list()
        for champion in f.readlines():
            loaded_champion = parse_dictionary_to_champion(json.loads(champion))
            add_champion(loaded_champion)
        f.close()
    except Exception as error:
        print("Some error occured during reading from file: {0}".format(error))


def save_data_to_file():
    try:
        f=open(filename, "w")
        for champion in get_champions():
            champStr = json.dumps(champion.get_champion_parsed_as_dictionary()) + "\n"
            f.write(champStr)
        f.close()
    except Exception as error:
        print("Some error occured during writing to a file: {0}".format(error))
