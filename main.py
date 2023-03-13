import random

from text import *

#important variables
inventory = []
got_food = False

#function to show inventory
def show_inventory():
	print("Your inventory contains:")
	for i in inventory:
		print(f"-{i.title()}")

#function to check choices against the possible choices
def check_choice(choices):
	choice = input("What is your choice?\n").lower().strip()
	while choice not in choices:
		print(f'\nInvalid command\nOptions: "{choices[0]}" or "{choices[1]}"')
		choice = input("What is your choice?\n").lower().strip()
	return choice

#scenario for forest.
def forest_scenario():
	scenario = random.randint(1, 3)
	if scenario == 1:
		print("You hear a loud noise.\nYou look around but don't see anything.")
	elif scenario == 2:
		print("You notice how muddy the ground is.")
	elif scenario == 3:
		print("You are starting to feel hungry and consider going back to the cabin to find food.")
	else:
		print("You are in a different part of the forest")

#Start Of Game

#print out the instructions
input('''Welcome to my game!
Here are the instructions:

** Use fullscreen terminal.

** Use commands to complete objectives in 
order to defeat the final boss.

** Only one word commands are accepted

** Make sure to type commands correctly.

** Have fun.

** Press enter to move on.
''')
#print out the commands
input('''Here are the commands:
north - move north
south - move south
east - move east
west - move west
up - move up
down - move down
inventory - view your inventory
use - use an item
grab - pick up an item
stay - stay where you are
goals - view your objectives
''')

#get the player's name
playername = input("What do you want your name to be?\n")
print(f"\nGood luck {playername},")
#print out the game title
input('''Welcome to

 _____  _             _____                       _   
|_   _|| |__    ___  |  ___|___   _ __  ___  ___ | |_ 
  | |  | '_ \  / _ \ | |_  / _ \ | '__|/ _ \/ __|| __|
  | |  | | | ||  __/ |  _|| (_) || |  |  __/\__ \| |_ 
  |_|  |_| |_| \___| |_|   \___/ |_|   \___||___/ \__|
		(Press enter to begin)\n''')
print("\n\n\n")

#Scenario for first time in cabin.
print("You wake up in a cabin bed, you don't know how you got here.\nThe clock beside you reads 10:30 PM.\nYou look outside the window, there is a dark forest.\nYou can exit to the north.\n")
choice = check_choice(["north", "stay"])
if choice == "north":
	print("\nYou go north and leave the cabin\nYou have entered the forest")
else:
	print("\nYou stay in bed and wake up the next morning.\n")

#forest scenario --- will get moved
forest_scenario()

#scenario for box of food.
if got_food == False:
	print("\nYou find a box in the forest.")
	choice = check_choice(["yes", "no"])
	if choice == "yes":
		print("\nYou open the box and find some food.")
		got_food = True
		inventory.append("Food")
		show_inventory()
	else:
		print("\nYou decide not to open the box.")
else:
	print("You are back at the box where you found food")

#scenario for guard interaction.
print(forest_guard)
choice = input(guard_choice)
while choice not in guard_choice_opt:
	print(f'\nInvalid command\nOptions: "{guard_choice_opt[0]}" or "{guard_choice_opt[1]}"\n')
	choice = input(guard_choice)
if choice == guard_choice_opt[0]:
	print(guard_approach)
	if "food" in inventory:
		guard_choice = input(guard_approach_choice)
		while guard_choice not in guard_approach_choice_opt:
			print(f'\nInvalid command\nOptions: "{guard_approach_choice_opt[0]}" or "{guard_approach_choice_opt[1]}"\n')
			choice = input(guard_approach_choice)
		if guard_choice == guard_approach_choice_opt[0]:
			print(guard_approach_give)
			inventory.remove("food")
			inventory.append(key_item)
			show_inventory()
		else:
			print(guard_approach_refuse)
	else:
		print(guard_approach_nofood)
else:
	print(guard_ignore)
	
#scenario for hatch
print(forest_hatch)
choice = input(hatch_choice)
while choice not in hatch_choice_opt:
	print(f'\nInvalid command\nOptions: "{hatch_choice_opt[0]}" or "{hatch_choice_opt[1]}"\n')
	choice = input(hatch_choice)
if choice == hatch_choice_opt[0]:
	print(hatch_open)
	if "key" in inventory:
		hatch_choice = input(hatch_open_keychoice)
		while hatch_choice not in keychoice_opt:
			print(f'\nInvalid command\nOptions: "{keychoice_opt[0]}" or "{keychoice_opt[1]}"\n')
			hatch_choice = input(hatch_open_keychoice)
		if hatch_choice == keychoice_opt[0]:
			print(hatch_open_yes)
			inventory.remove("key")
		else:
			print(hatch_open_no)
	else:
		print(hatch_open_nokey)
else:
	print(hatch_leave)
