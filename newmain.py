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
"cabin": [["north", "forest"]],
"forest": [["north", "clear"],["south", "cabin"],["west", "camp"]],  
"camp": [["east", "forest"]],
"clear": [["north", "deer"],["east", "noise"],["south", "forest"]],
"key": [["north", "swamp"]],
"swamp": [["south", "key"],["east", "deer"]],
"deer": [["south", "clear"],["west", "swamp"]],
"noise": [["south", "food"],["west", "clear"]],
"food": [["north", "noise"],["east", "feet"]],
"feet": [["north", "dark"],["west", "food"]],
"dark": [["south", "feet"],["north", "dog"]],
"dog": [["south", "dark"],["west", "hatch"]],
"hatch": [["west", "dog"],["down", "bunker"]],
"bunker": [["up", "hatch"]]
}

descriptions = {
"cabin": "You are in a small cabin. There is a table with a map and a flashlight on it.",
"forest": "You are in a forest. There are trees all around you.",
"camp": "You found an abandoned campsite. There is a tent and a fire pit.",
"clear": "You are in a clearing. There are some bushes and a pile of rocks.",
"key": "You found a key on the ground.",
"swamp": "You are in a swamp. The ground is wet and slippery.",
"deer": "You found a watering hole. There are some deer nearby.",
"noise": "You are in a forest. You think you hear a machine.",
"food": "You found a stash of canned food. It looks like it's been here for a while.",
"feet": "You hear some footsteps. There might be someone following you.",
"dark": "You are in a dense forest. It's so dark it's hard to see where you're going.",
"dog": "You found an old house. Before you go inside a dog comes out.",
"hatch": "You found a metal hatch. There is a padlock on it.",
"bunker": "You are in the bunker."
}

grab_items = {
"cabin": "flashlight",
"food": "can of food",
"key": "key",
"clear": "rock",
"bunker": "trophy",
"dog": "dog"
}

use_items = {
"hatch": "key",
"dark": "flashlight",
"deer": "rock",
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
		print(f"There is a {grab_items[self.__location]} here.")

	@property
	def location(self):
		return self.__location

	@location.setter
	def location(self, new_location):
		self.__location = new_location

	def dark(self):
		if "flashlight" in self.inventory:
			self.use(self.__location)
		else:
			print("You get lost and find yourself at an abandoned campsite.")
			self.check_item("camp")
			self.__location = "camp"
		return self.location

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
			if grab_items[current]:
				print(f"There is a {grab_items[current]} here.")
		except:
			pass

	def grab(self, current):
		try:
			if grab_items[current]:
				self.inventory.append(grab_items[current])
			print(f"You pick up {grab_items[current]}.\n")
			del grab_items[current]
			print("Inventory:")
			for i in self.inventory:
				print(f"- {i.title()}")
		except:
			print("There is nothing here to pick up.")

	def use(self, current):
		if self.inventory != []:
			try:
				print("\nWhat would you like to use?")
				choice = self.check_choice(self.inventory)
				if choice == use_items[current]:
					self.inventory.remove(use_items[current])
					print(f"You used {use_items[current]}.")
					if self.inventory != []:
						print("Inventory:")
						for i in self.inventory:
							print(f"- {i.title()}")
					else:
						print("Inventory is now empty.")
				else:
					print(f"You cannot use {choice}.")
			except:
				print("You cannot use that here.")
		else:
			print("Inventory is empty.")
		return current

def save(player):
	with open("save_game.txt", "wb") as file:
		pickle.dump(player, file)
		print("Game Saved!")

def load():
	with open("save_game.txt", "rb") as file:
		player = pickle.load(file)
		print("Game Loaded!")
		print(descriptions[player.location])
	return player

def quit():
	print("Thanks for playing!")

player = Player()
choice = None
while choice != "quit":
	choice = player.check_choice(["quit", "move", "save", "load", "grab", "use"])
	if choice == "quit":
		quit()
	elif choice == "move":
		player.location = player.movement(player.location)
		player.check_item(player.location)
		if player.location == "dark":
			player.dark()
	elif choice == "save":
		save(player)
	elif choice == "load":
		player = load()
	elif choice == "grab":
		player.grab(player.location)
	elif choice == "use":
		player.use(player.location)
