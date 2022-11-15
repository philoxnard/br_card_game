class CommandParser():

	def handleParsedMessage(self, message):

		print('inside client side command parser')

		command = message["command"]

		if command == "affirm_connection":

			result = self.handleAffirmedConnection(message)

		elif command == "add_player_to_lobby":

			result = self.handleSampleMessage(message)

		else:

			result = {"command" : "error, the command doesnt have a handler"}
			print('command doesnt have handler')
			print('this message couldnt be parsed:')
			print(message)

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

		result = {}
		command = "sample messa"
		result["command"] = command

		return result