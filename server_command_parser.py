from lobby import Lobby

class CommandParser():

	def __init__(self):

		# the player waiting list and the func that creates unique ids should prob
		# be in a server tools doc or something like that
		self.players_waiting_for_game = []

	def handleParsedMessage(self, message):

		print('back end is handling this message')
		print(message)

		command = message["command"]

		if command == "check_if_connected":

			response = self.handleConnectionCheck(message)

		elif command == "add_player_to_lobby":

			response = self.handleAddPlayerToLobby(message)

		elif command == "check_for_full_lobby":

			response = self.checkIfPlayerLobbyIsFull(message)

		else:

			response = {}
			response["command"] = "couldnt parse message from client"

		return response

	def handleConnectionCheck(self, incomingMessage):

		response = {}
		# maybe assign unique id here
		command = "assign_unique_id"
		unique_id = "zxcv"
		response["command"] = command
		response["unique_id"] = unique_id

		return response

	def handleAddPlayerToLobby(self, incomingMessage):
		"""
		This function will put the player that initiated the message into a lobby, which will eventually
		become a game once we have enough players
		"""
		response = {}

		unique_id = incomingMessage["unique_id"]

		self.players_waiting_for_game.append(unique_id)

		response["command"] = "sample text"

		return response

	def checkIfPlayerLobbyIsFull(self, incomingMessage):

		unique_id = incomingMessage["unique_id"]

		response = {}

		if len(self.players_waiting_for_game) > 0:

			response["command"] = "set_state_to_in_game"

		else:

			response["command"] = "keep_waiting"

		return response