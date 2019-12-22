class Champion:
    def __init__(self, name, matches, souls, stats, game_time):
        self.name = name
        self.matches = matches
        self.souls = souls
        self.stats = stats
        self.game_time = game_time

    def get_champion_parsed_as_dictionary(self):
        result = {
            "name": self.name,
            "matches": self.matches,
            "souls": self.souls,
            "stats": self.stats,
            "game_time": self.game_time
        }
        return result