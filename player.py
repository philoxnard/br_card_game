from realm import Realm
import identities
import sample_decks

class Player():

	def __init__(self, name, deck, identity):

		self.deck = deck
		self.hand = []

		self.starting_life = identity.starting_life
		self.current_life = self.starting_life

		self.starting_hand_size = identity.starting_hand_size
		self.current_hand_size = self.starting_hand_size
		self.draw_starting_hand()

		self.devoted_cards = []
		self.current_devotion = 0
		self.available_devotion = 0

		self.name = name

		self.realm = Realm()
		self.enemy_realm = None

		self.identity = identity

	def print_hand(self):

		print('your hand is: ')
		for card in self.hand:
			print(card.name)

	def draw_starting_hand(self):
		for i in range(self.starting_hand_size):
			self.draw()

	def take_turn(self):

		self.upkeep_phase()
		self.draw_phase()
		self.devote_phase()
		self.play_phase()

		print('ending turn')
		print()

	def upkeep_phase(self):

		print()
		print()
		print("starting " + self.name + "'s turn")
		print("your devotion is " + str(self.current_devotion))
		print("in your realm: ")
		print("your battle queue: " + str(self.realm.protector_battle_queue))
		print("your enemeys battle queue: " + str(self.realm.invader_battle_queue))

		print()
		print('in your enemys realm:')
		print("your battle queue: " + str(self.enemy_realm.invader_battle_queue))
		print("your opponent's battle queue : " + str(self.enemy_realm.protector_battle_queue))
		print()

	def draw_phase(self):

		if self.deck != []:

			self.draw()

			self.print_hand()

		else:

			print("you lose, no cards left")

	def draw(self):

		drawn_card = self.deck.pop(0)
		self.hand.append(drawn_card)

	def devote_phase(self):

		check_devote = input("do you want to devote? type no for no, otherwise type card index you want to devote ")
		print()
		if check_devote == "no":

			return

		else:

			self.devote_card(check_devote)

	def devote_card(self, devotedIndex):

		devotedIndex = int(devotedIndex)
		devoted_card = self.hand.pop(devotedIndex)
		print('devoting ' + devoted_card.name)
		print()
		self.devoted_cards.append(devoted_card)
		self.current_devotion = len(self.devoted_cards)
		self.available_devotion = self.current_devotion

		print("your devotion is now " + str(self.current_devotion))

	def play_phase(self):

		self.print_hand()
		check_play = input("do you want to play a card? type no for no, otherwise type card index you want to play ")
		print()
		if check_play == "no":

			return

		else:

			is_play_legal = self.check_if_play_is_legal(check_play)
			if is_play_legal == True:
				self.play_card(check_play)

	def check_if_play_is_legal(self, playIndex):

		playIndex = int(playIndex)
		card_to_be_played = self.hand[playIndex]
		if card_to_be_played.cost <= self.available_devotion:
			print('card is legal')
			return True
		else:
			print('not enough devotion')
			return False

	def play_card(self, playIndex):

		where_to_play = input("play this card as invader or protector? ")
		print()
		playIndex = int(playIndex)
		card_to_be_played = self.hand.pop(playIndex)

		if where_to_play == "protector":
			self.realm.protector_battle_queue.append(card_to_be_played)

		else:
			self.enemy_realm.invader_battle_queue.append(card_to_be_played)

		self.available_devotion = self.available_devotion - card_to_be_played.cost

		print('you now have ' + str(self.available_devotion) + ' available devotion')
		print('your battle queue is this:')
		for card in self.realm.protector_battle_queue:
			print(card.name)

if __name__ == "__main__":

	player1 = Player("player_one", sample_decks.sample_deck_one, identities.barshk)
	player2 = Player("player_two", sample_decks.sample_deck_one, identities.barshk)

	player1.enemy_realm = player2.realm
	player2.enemy_realm = player1.realm

	player1.take_turn()
	player2.take_turn()
	player1.take_turn()
	player2.take_turn()
	player1.take_turn()
	player2.take_turn()
	player1.take_turn()
	player2.take_turn()