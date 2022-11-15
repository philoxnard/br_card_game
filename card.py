class Card():

	def __init__(self, name, type, cost, tribe=None, effect=None, health=None, power=None):

		self.name = name
		self.type = type
		self.cost = cost
		self.tribe = tribe
		self.effect = effect
		self.health = health
		self.power = power

		self.ready_to_attack = True
		self.alive = True

	def check_for_death(self):

		if self.health < 0:

			self.health = 0

			self.die()

	def die(self):

		self.alive = False

	def attack_creature(self, defender):

		defender.health = defender.health - self.power
		self.ready_to_attack = False

		if defender.health <= 0:
			defender.health = 0
			defender.die()

	def attack_player(self):

		self.ready_to_attack = False