class Champion:
    def __init__(self, id, name, matches, souls, stats, game_time):
        self.id = id
        self.name = name
        self.matches = matches
        self.souls = souls
        self.stats = stats
        self.game_time = game_time

    def get_champion_parsed_as_dictionary(self):
        result = {
            "id": self.id,
            "name": self.name,
            "matches": self.matches,
            "souls": self.souls,
            "stats": self.stats,
            "game_time": self.game_time
        }
        return result


def parse_dictionary_to_champion(dictionary):
    parsed_champion = Champion(id=dictionary["id"],
                               name=dictionary["name"],
                               matches=dictionary["matches"],
                               souls=dictionary["souls"],
                               stats=dictionary["stats"],
                               game_time=dictionary["game_time"])
    return parsed_champion
