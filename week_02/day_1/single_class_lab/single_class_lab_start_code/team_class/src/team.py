class Team:
    def __init__(self, get_name, get_players, get_coach):
        self.name = get_name
        self.players = get_players
        self.coach = get_coach
        self.points = 0

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player_to_find):
        player_exists = False
        for player in self.players:
            if player == player_to_find:
                player_exists = True

        return player_exists
    
    def play_game(self, result):
        if result == True:
            self.points += 3
