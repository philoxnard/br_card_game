class Deck():

	def __init__(self, decklist):

		self.starting_deck_size = len(decklist)
		self.current_deck_size = self.starting_deck_size

		self.decklist = decklist