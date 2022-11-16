# import kivy module
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import time

from threading import Thread

from functools import partial

import client_network
import screen_manager

class BoxLayoutApp(App):

	def build(self):
		"""
		This is essentially the __init__ function. This is called when the BoxLayoutApp is initialized
		"""

		print('initializing front end')

		self.network = client_network.Network()
		self.commandParser = self.network.commandParser
		self.screen = screen_manager.ScreenManager()

		self.unique_id = None
		self.state = "initializing"

		self.server_pinger = Thread(target = self.ping_server, args=(1, ))
		self.server_pinger.start()

		# We'll check to see if we've successfully connected to the server
		# If we're connected, we'll go straight to the login page
		self.connected = False
		while self.connected == False:

			try:

				unique_id = self.network.check_connection()
				if unique_id != None:

					self.unique_id = unique_id
					# This should always be the chunk of code that fires unless the server is off

					drawn_screen = self.on_connect()
					self.connected = True

				else:

					# If the server is off, this will fire
					drawn_screen = self.failed_to_connect_to_server()
					break

			except Exception as e:

				# If something is weird then this will fire, idk when it would.
				drawn_screen = self.cannot_connect_to_server(e)

		return drawn_screen

	def ping_server(self, num):

		while True:

			if self.state == "waiting_for_game":

				message = {}
				command = "check_for_full_lobby"
				unique_id = self.unique_id
				message["command"] = command
				message["unique_id"] = unique_id

				response = self.network.send(message)

				print('in ping server after response')
				print(response)

				if response["command"] == "set_state_to_in_game":

					print('entering game')
					self.enter_game()

				# self.commandParser.handleParsedMessage(response, self.screen)

			time.sleep(1)


	def login(self, username, event):

		self.username = username
		drawn_screen = self.screen.draw_main_menu(self.username)
		self.screen.play_solo_button.bind(on_press = partial(self.select_deck_screen, self.username))
		return drawn_screen

	def select_deck_screen(self, username, event):

		self.screen.draw_select_deck_screen(username)
		self.screen.select_barshk_deck.bind(on_press=partial(self.search_for_game, "a full decklist, separated by commas"))
		# self.screen.select_barshk_deck.bind(on_press=partial(self.enter_game, "a full decklist, separated by commas"))

	def search_for_game(self, decklist, event):

		print('selected')
		print(decklist)
		self.screen.draw_searching_for_game_screen()


		self.state = "waiting_for_game"
		# Feels like this should be somewhere else but idk yet
		message = {}
		message["command"] = "add_player_to_lobby"
		message["unique_id"] = self.unique_id

		self.network.send(message)

	def failed_to_connect_to_server(self):

		drawn_screen = self.screen.failed_to_connect_screen()
		return drawn_screen

	def cannot_connect_to_server(self, error):

		print(error)
		drawn_screen = self.screen.draw_no_connection_screen(error)
		return drawn_screen

	def on_connect(self):

		drawn_screen = self.screen.draw_welcome_screen()
		self.screen.login_button.bind(on_press = partial(self.login, 'Guest'))
		return drawn_screen

	def loading_screen(self, event):

		self.screen.draw_loading_screen()

	def enter_game(self, decklist, event):

		self.screen.draw_sample_game_screen()

root = BoxLayoutApp()

root.run()

if __name__ == "__main__":

	box = BoxLayoutApp()
	box.run()