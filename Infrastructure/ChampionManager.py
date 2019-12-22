championsDB = []


def add_champion(new_champion):
    if new_champion.id is None or new_champion.id <= 0:
       new_champion.id = get_champion_id()
    championsDB.append(new_champion)


def get_champions():
    return championsDB


def edit_champion(champion):
    for champ in championsDB:
        if champ.id == champion.id:
            assign_values(champ, champion)


def assign_values(champion_from_db, new_champion):
    champion_from_db.name = new_champion.name
    champion_from_db.matches = new_champion.matches
    champion_from_db.souls = new_champion.souls
    champion_from_db.stats = new_champion.stats
    champion_from_db.game_time = new_champion.game_time


def get_champion_id():
    minId = 0
    for champ in championsDB:
        if champ.id < minId:
            minId = champ.id
    return minId
