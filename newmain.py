


import pickle

start = '''\nWelcome to
 _____  _             _____                       _   
|_   _|| |__    ___  |  ___|___   _ __  ___  ___ | |_ 
  | |  | '_ \  / _ \ | |_  / _ \ | '__|/ _ \/ __|| __|
  | |  | | | ||  __/ |  _|| (_) || |  |  __/\__ \| |_ 
  |_|  |_| |_| \___| |_|   \___/ |_|   \___||___/ \__|

Here are your commands:
quit - leave the game
save - save the game
load - load game from last save
use  - use an item from you inventory
grab - pickup an item
move - display movement options
		(Press enter to begin)\n\n'''

locations = {
"cabin": [["north", "f6"]],
"f6": [["north", "f3"],["south", "cabin"],["east", "food"],["west", "f5"]],  
"food": [["north", "f4"],["west", "f6"]],
"f5": [["north", "key"],["east", "f6"]],
"key": [["north", "f1"],["south", "f5"],["east", "f3"]],
"f3": [["north", "f2"],["south", "f6"],["east", "f4"],["west", "key"]],
"f4": [["north", "hatch"],["south", "food"],["west", "f3"]],
"f1": [["south", "key"],["east", "f2"]],
"f2": [["south", "f3"],["east", "hatch"],["west", "f1"]],
"hatch": [["south", "f4"],["west", "f2"],["down", "bunker"]],
}

descriptions = {
"cabin": "You are in a small cabin. There is a table with a map and a flashlight on it.",
"f6": "You are in a forest. There are trees all around you.",
"food": "You found a stash of canned food. It looks like it's been here for a while.",
"f5": "You found an abandoned campsite. There is a tent and a fire pit.",
"key": "You found a key on the ground.",
"f3": "You are in a clearing. There are some bushes and a pile of rocks.",
"f4": "You are in a forest. You think you hear a machine.",
"f1": "You are in a swamp. The ground is wet and slippery.",
"f2": "You are in a dense forest. It's hard to see where you're going.",
"hatch": "You found a metal hatch. There is a padlock on it.",
"bunker": "You are in the bunker"
}

items = {
"cabin": "flashlight",
"food": "can of food",
"key": "key",
"f3": "rock",
"bunker": "trophy"
}


class Player():
	'''A player object'''
	def __init__(self):
		self.__location = "cabin"
		self.inventory = []
		name = input("What is your name?\n")
		print(f"Good luck {name},")
		input(start)
		print(descriptions[self.__location])
		print(f"There is a {items[self.__location]} here.")

	@property
	def location(self):
		return self.__location

	@location.setter
	def location(self, new_location):
		self.__location = new_location

	def movement(self, current):
		num = 0
		choice_list = []
		for i in locations[current]:
			moves = locations.get(current)[num][0]
			choice_list.append(moves)
			num += 1
		move = self.check_choice(choice_list)
		for i in locations[current]:
			if i[0] == move:
				new_location = i[1]
				self.__location = new_location
				print(descriptions[new_location])
				return new_location

	def check_choice(self, choices):
		print('\nOptions:')
		num = 0
		for i in choices:
			print(f"- {choices[num].title()}")
			num += 1
		choice = input('\n').lower().strip()
		while choice not in choices:
			print('\nInvalid command\nOptions:')
			num = 0
			for i in choices:
				print(f"- {choices[num].title()}")
				num += 1
			choice = input('').lower().strip()
		return choice
	
	def check_item(self, current):
		try:
			if items[current]:
				print(f"There is a {items[current]} here.")
		except:
			print("There is nothing here.")


	def grab(self, current):
		pass 										#I AM HERE RIGHT NOW

def save(player):
	with open("save_game.txt", "wb") as file:
		pickle.dump(player, file)
		print("Game Saved!")

def load():
	with open("save_game.txt", "rb") as file:
		player = pickle.load(file)
		print("Game Loaded!")
	return player

def quit():
	print("Thanks for playing!")

player = Player()
choice = None
while choice != "quit":
	choice = player.check_choice(["quit", "move", "save", "load", "grab"])
	if choice == "quit":
		quit()
	elif choice == "move":
		player.location = player.movement(player.location)
		player.check_item(player.location)
	elif choice == "save":
		save(player)
	elif choice == "load":
		player = load()
	elif choice == "grab":
		pass
