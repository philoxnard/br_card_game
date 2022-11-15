from card import Card
import card_effects

class Realm():

	def __init__(self):

		self.protector_battle_queue = []
		self.invader_battle_queue = []

		self.graveyard = []

	def execute_combat(self):

		self.combat_over = False

		while self.combat_over == False:

			self.get_combatants()

			self.execute_attack()

			self.clean_up_dead_cards()
			print()

		self.prime_cards_for_next_combat()

		print("combat is over")

	def get_combatants(self):

			# Defender is the first card in the protector's battle queue
			# If the protector has no cards in the battle queue, this returns None
			self.protector_defender = self.get_current_defender(self.protector_battle_queue)
			self.invader_defender = self.get_current_defender(self.invader_battle_queue)

			# Attacker is the current attacker in the battle queue
			# If the protector has fewer cards in the battle queue than their invader, this may return None
			self.protector_attacker = self.get_current_attacker(self.protector_battle_queue)
			self.invader_attacker = self.get_current_attacker(self.invader_battle_queue)

			if self.protector_attacker:
				print("protector attacker this round is " + self.protector_attacker.name)
			else:
				print("protector has no attacker this round")
			if self.protector_defender:
				print("protector defender this round is " + self.protector_defender.name)
			else:
				print("protector has no defender this round")
			if self.invader_attacker:
				print("invader attacker this round is " + self.invader_attacker.name)
			else:
				print("invader has no attacker this round")
			if self.invader_defender:
				print("invader defender this round is " + self.invader_defender.name)
			else:
				print("invader has no defender this round")

	def execute_attack(self):

		# First, let's just check for all the conditions that would lead to combat being over
		if self.protector_attacker == None and self.invader_attacker == None:

			self.combat_over = True

		if self.invader_defender == None:

			self.combat_over = True

		# Now, let's check to see if the invader gets a direct hit

		if self.invader_attacker != None and self.protector_defender == None:

			self.invader_attacker.attack_player()
			print("invader's " + self.invader_attacker.name + " attacks directly for " + str(self.invader_attacker.power))

		# Next, let's check to see if cards need to attack each other

		if self.invader_attacker != None and self.protector_defender != None:

			self.invader_attacker.attack_creature(self.protector_defender)
			print("invader's " + self.invader_attacker.name + " attacks your " + self.protector_defender.name + " for " + str(self.invader_attacker.power))

		if self.protector_attacker != None and self.invader_defender != None:

			self.protector_attacker.attack_creature(self.invader_defender)
			print("your " + self.protector_attacker.name + " attacks invader's " + self.invader_defender.name + " for " + str(self.protector_attacker.power))

	def get_current_defender(self, battleQueue):

		if battleQueue != []:

			return battleQueue[0]

		else:

			return None

	def get_current_attacker(self, battleQueue):

		for card in battleQueue:

			if card.ready_to_attack == True:

				return card

		return None

	def clean_up_dead_cards(self):

		for card in self.protector_battle_queue:

			if card.alive == False:

				print(card.name + " has died")
				self.protector_battle_queue.remove(card)
				self.graveyard.append(card)

		for card in self.invader_battle_queue:

			if card.alive == False:

				print(card.name + " has died")
				self.invader_battle_queue.remove(card)
				self.graveyard.append(card)

	def prime_cards_for_next_combat(self):

		for card in self.protector_battle_queue:
			card.ready_to_attack = True

		for card in self.invader_battle_queue:
			card.ready_to_attack = True

if __name__ == "__main__":

	realm = Realm()

	card1 = Card(name="zergling", type="creature", cost=1, tribe="zerg", effect=card_effects.zergling, health=1, power=1)
	card2 = Card(name="knight", type="creature", cost=1, tribe="zerg", effect=card_effects.zergling, health=2, power=2)
	card3 = Card(name="rager", type="creature", cost=1, tribe="zerg", effect=card_effects.zergling, health=1, power=3)
	card4 = Card(name="wall", type="creature", cost=1, tribe="zerg", effect=card_effects.zergling, health=4, power=0)
	card5 = Card(name="zergling", type="creature", cost=1, tribe="zerg", effect=card_effects.zergling, health=1, power=1)


	print('simulating combat')
	print()


	realm.protector_battle_queue = [card3, card4, card5]
	# realm.protector_battle_queue = []



	realm.invader_battle_queue = [card1, card2]
	# realm.invader_battle_queue = []

	realm.execute_combat()