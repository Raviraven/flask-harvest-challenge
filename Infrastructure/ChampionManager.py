championsDB = []


def add_champion(new_champion):
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
