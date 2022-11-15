class Game():

	def __init__(self, players):

		self.players = players
		self.living_players = self.players
		self.starting_player_count = len(self.players)
		self.current_player_count = self.starting_player_count

		self.number_of_players = len(self.starting_player_count)

		self.assign_enemy_realms()

	def run(self):

		self.take_player_turns()
		self.execute_combat()
		self.check_for_dead_player()

	def assign_enemy_realms(self):

		for player_index in range(self.number_of_players):

			player = self.players[player_index]

			if player_index == self.number_of_players - 1:
				enemy_index = 0

			else:
				enemy_index = player_index + 1

			enemy = self.players[enemy_index]
			player.enemy_realm = enemy.realm

	def take_player_turns(self):

		for player in self.players:

			player.take_turn()

	def execute_combat(self):

		for player in self.players:

			realm = player.realm

			realm.execute_combat()

	def check_for_dead_player(self):

		new_living_player_list = []
		for player in self.living_players:
			pass