import pickle

COMMANDS = '''Here are your commands:
quit - leave the game
save - save the game
load - load game from last save
use  - use an item from you inventory
grab - pickup an item
move - desplay movement options'''

class Player():
	'''A player'''
	def __init__(self, location = "Home"):
		self.location = location


def quit(save):
	if save == False:
		i = input("Do you want to save the game?\n")
		if i.lower() == "yes":
			save()
	print("Thanks for playing!")

def save():
	i = input("Do you already have a save file?\n")
	if i.lower() == "yes":
		name = input("What is the name of the save file?\n")
	else:
		name = input("What do you want to name the save file?\n")
	with open(name, "wb") as file:
		pickle.dump(Player, file)

def load():
	name = input("What is the name of the save file?\n")
	with open(name, "rb") as file:
		pickle.load(file)
save()
