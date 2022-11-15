from player import Player
from game import Game

import sample_decks
import identities


if __name__ == '__main__':

	player_1 = Player("player_one", sample_decks.sample_deck_one, identities.aloona)
	player_2 = Player("player_two", sample_decks.sample_deck_two, identities.barshk)

	players = [player_1, player_2]

	game = Game(players)

	game.run()