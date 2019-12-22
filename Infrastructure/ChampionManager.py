championsDB = []



def clear_champions_list():
    championsDB.clear()


def add_champion(new_champion):
    if new_champion.id is None or new_champion.id <= 0:
       new_champion.id = get_champion_id()
    championsDB.append(new_champion)


def get_champions():
    return championsDB


def edit_champion(champion):
    for champ in championsDB:
        if str(champ.id) == str(champion.id):
            assign_values(champ, champion)


def delete_champion(champion_id):
    for champ in championsDB:
        if str(champ.id) == str(champion_id):
            championsDB.remove(champ)


def assign_values(champion_from_db, new_champion):
    champion_from_db.name = new_champion.name
    champion_from_db.matches = new_champion.matches
    champion_from_db.souls = new_champion.souls
    champion_from_db.stats = new_champion.stats
    champion_from_db.game_time = new_champion.game_time


def get_champion_id():
    maxId = 0
    for champ in championsDB:
        if champ.id > maxId:
            maxId = champ.id
    return maxId + 1
