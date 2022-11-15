"""

The server needs to:
1) listen for new connections
2) allow new connections to log on
3) allow new connections to pick their deck
4) put players into lobby
5) play game

"""

import socket
import json
from _thread import *
from server_command_parser import CommandParser
from game_manager import GameManager

class Server():

	def __init__(self):

		self.server = "127.0.0.1"
		self.port = 54553

		self.gameManager = GameManager()
		self.commandParser = CommandParser()

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.open_server()

	def open_server(self):

		try:

			self.sock.bind((self.server, self.port))
			print('server opened')
			self.sock.listen()

		except socket.error as e:
			print(e)

	def threaded_client(self, connection):
		"""
		This gets called whenever we receive a new connection. This starts a new thread.
		"""

		reply = ""
		while True:
			try:

				# We constantly check to see if we're receiving data
				data = connection.recv(2048)

				# If we aren't receiving data, we'll kill the thread bc they disconnected
				if not data:
					print("Disconnected")
					break
				else:

					response_message = self.handleIncomingMessage(connection, data)
					connection.sendall(response_message)

			except Exception as e:
				print(e)
				break

		print("Lost connection, closing the socket and ending the thread")
		connection.close()

	def handleIncomingMessage(self, connectionObject, data):
		"""
		This will handle messages that come to the server from the client. First we'll decode bc it'll
		come in as bytes, then we'll json.loads bc that string will be a stringified object, then we'll
		read the command and act accordingly.
		"""
		# We're also going to pass the connection object in here, idk if its necessary or not?

		# Decode and load the received message so we can turn it into a digestible dictionary
		decoded_data = data.decode('utf-8')
		message = json.loads(decoded_data)

		# Again, not sure if this is helpful, but we'll add it
		message["connection_object"] = connectionObject

		# This will also always respond with a dictionary with a ["command"] key so the front knows what
		# to do with it
		response = self.commandParser.handleParsedMessage(message)

		print('sending response back to front:')
		print(response)

		dumped_response = json.dumps(response)
		encoded_response = dumped_response.encode('utf-8')

		return encoded_response

	def run(self):

		while True:

			connection, address = self.sock.accept()

			print("connected to ")
			print(address)

			start_new_thread(self.threaded_client, (connection,))

if __name__ == "__main__":

	server = Server()
	server.run()