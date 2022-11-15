import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ScreenManager():

	def __init__(self):

		self.superBox = BoxLayout(orientation = "vertical")

	def failed_to_connect_screen(self):

		self.attempting_to_connect_label = Label(text="Failed to connect, server probably isn't running or you're looking for the wrong IP")

		self.superBox.add_widget(self.attempting_to_connect_label)
		return self.superBox

	def draw_no_connection_screen(self, error):

		self.no_connection_label = Label(text="Can't connect to server")
		self.error_label = Label(text=str(error))

		self.superBox.add_widget(self.no_connection_label)
		self.superBox.add_widget(self.error_label)
		return self.superBox

	def draw_welcome_screen(self):

		self.title_banner = Label(text="Welcome to battle royale card game")
		self.login_button = Button(text = "Click to log in with the name 'Guest'")

		self.superBox.add_widget(self.title_banner)
		self.superBox.add_widget(self.login_button)

		return self.superBox

	def draw_main_menu(self, username):

		self.superBox.remove_widget(self.login_button)

		self.username_indicator = Label(text = "You are playing as " + username)
		self.play_solo_button = Button(text = "Play Solo")
		self.play_as_team_botton = Button(text ="Play With Team (Coming soon)")
		self.view_collection_button = Button(text ="View Collection/Deck Build (Coming soon)")

		self.superBox.add_widget(self.username_indicator)
		self.superBox.add_widget(self.play_solo_button)
		self.superBox.add_widget(self.play_as_team_botton)
		self.superBox.add_widget(self.view_collection_button)

		return self.superBox

	def draw_select_deck_screen(self, username):

		self.superBox.clear_widgets()

		self.select_your_deck = Label(text="select your deck, " + username)
		self.select_barshk_deck = Button(text="Play with barshk deck")
		# self.select_aloona_deck = Button(text="Play with aloona deck")

		self.superBox.add_widget(self.select_your_deck)
		self.superBox.add_widget(self.select_barshk_deck)
		# self.superBox.add_widget(self.select_aloona_deck)

		return self.superBox

	def draw_loading_screen(self):

		self.superBox.clear_widgets()

		self.loading = Label(text = "Loading")

		self.superBox.add_widget(self.loading)

	def draw_searching_for_game_screen(self):

		self.superBox.clear_widgets()

		self.searching_for_game_label = Label(text = "Searching for game")

		self.superBox.add_widget(self.searching_for_game_label)

	def draw_sample_game_screen(self):

		self.superBox.clear_widgets()

		self.prey_box = BoxLayout(orientation ='horizontal')
		self.your_box = BoxLayout(orientation ='horizontal')
		self.ui_box = BoxLayout(orientation ='horizontal')

		self.prey_realm = Label(text="this is your prey's realm")
		self.your_realm = Label(text="this is your realm")
		self.your_info = Label(text="this is your hand/devotion/health/identity")

		self.prey_box.add_widget(self.prey_realm)
		self.your_box.add_widget(self.your_realm)
		self.ui_box.add_widget(self.your_info)

		self.a_card = Label(text="it'll contain multiple cards")
		self.prey_box.add_widget(self.a_card)

		self.superBox.add_widget(self.prey_box)
		self.superBox.add_widget(self.your_box)
		self.superBox.add_widget(self.ui_box)

		return self.superBox