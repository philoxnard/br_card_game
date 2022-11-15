class CommandParser():

	def handleParsedMessage(self, message):

		print('inside client side command parser')

		command = message["command"]

		if command == "affirm_connection":

			result = self.handleAffirmedConnection(message)

		elif command == "add_player_to_lobby":

			result = self.handleSampleMessage(message)

		return result

	def handleAffirmedConnection(self, incomingMessage):

		result = {}
		command = "affirm_connection"
		result["command"] = command

		return result

	def handleSampleMessage(self, incomingMessage):

		text = incomingMessage["text"]

		print('received the sample message:')
		print(text)