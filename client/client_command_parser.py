class CommandParser():

	def handleParsedMessage(self, message, screen=None):

		print('inside client side command parser')

		command = message["command"]

		if command == "assign_unique_id":

			print("gonna try to assign unique id")
			result = self.handleAssignedUniqueID(message)

		elif command == "set_state_to_in_game":

			result = self.handleSetStateToInGame(message, screen)

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

	def handleAssignedUniqueID(self, incomingMessage):

		return incomingMessage

	def handleSetStateToInGame(self, incomingMessage, screen):

		print('gonna try to draw new screen')
		if screen != None:

			print('did we draw the screen')
			screen.draw_sample_game_screen()

		result = {}
		command = "tried to draw new screen"
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