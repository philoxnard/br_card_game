import socket
import json
import time

import client_command_parser

class Network():

	def __init__(self):

		print('initializing network object')

		self.commandParser = client_command_parser.CommandParser()

		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = "127.0.0.1"
		self.port = 54553
		self.address = (self.server, self.port)

		self.is_connection_established = self.connect()

	def connect(self):

		try:

			self.client.connect(self.address)

			message = {}
			command = "check_if_connected"
			message["command"] = command

			result = self.send(message)

			# If we got the expected result, then we know we're connected
			if result["command"] == "affirm_connection":

				return True

			else:

				return False

		except Exception as e:
			print(e)
			return False

	def check_connection(self):

		return self.is_connection_established

	def send(self, data):
		"""
		The standard function used for sending data from front end to back end
		"""

		try:

			dumped_message = json.dumps(data)
			encoded_data = dumped_message.encode('utf-8')
			self.client.send(encoded_data)

			# We then grab the response from the server
			response_message = self.client.recv(2048)

			parsed_message = self.parseIncomingMessage(response_message)

			result = self.commandParser.handleParsedMessage(parsed_message)

			return result

		except socket.error as e:
			print(e)

	def parseIncomingMessage(self, message):
		"""
		This function will parse message sent from the back end.
		"""

		# First, we need to decode the bytes into a string
		decoded_message = message.decode('utf-8')

		# Then, we convert it from a string into an object
		loaded_message = json.loads(decoded_message)

		# Then we can return it
		return loaded_message

if __name__ == "__main__":

	network = Network()