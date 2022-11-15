from lobby import Lobby

class CommandParser():

	def __init__(self):

		self.lobby = None

	def handleParsedMessage(self, message):

		print('back end is handling this message')
		print(message)

		command = message["command"]

		if command == "check_if_connected":

			response = self.handleConnectionCheck(message)

		elif command == "add_player_to_lobby":

			response = self.handleAddPlayerToLobby(message)

		return response

	def handleConnectionCheck(self, incomingMessage):

		response = {}
		command = "affirm_connection"
		response["command"] = command

		return response

	def handleAddPlayerToLobby(self, incomingMessage):
		"""
		This function will put the player that initiated the message into a lobby, which will eventually
		become a game once we have enough players
		"""
		response = {}
		connection_object = incomingMessage["connection_object"]
		print('whats in connection object')
		print(connection_object)

		# if self.lobby == None:

		# 	self.lobby = Lobby()

		# if self.lobby.current_size == self.lobby.max_size:
			# Lobby is full and we'll create a game out of it
			# player_list = self.lobby.create_game()


		command = "send_players_to_game"

		response["command"] = command
		# response["player_list"] = player_list


		# else:
		# 	self.lobby.add_player(connection_object)



		return response