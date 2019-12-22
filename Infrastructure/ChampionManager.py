import Models.Champion

championsDB = []


def add_champion(new_champion):
    championsDB.append(new_champion)


def get_champions():
    return championsDB
