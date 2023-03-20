import random

#important variables
inventory = []
got_food = 0
guard_approached = 0
hatch_opened = 0
complete = 0
started = 0
current = "f6"

#locations dictionary
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
"hatch": [["south", "f4"],["west", "f2"]],
}

#function for movement
def movement(current):
	print("\nYou can move:")
	num = 0
	choice_list = []
	for i in locations[current]:
		moves = locations.get(current)[num][0]
		choice_list.append(moves)
		print("- " + moves)
		num += 1
	print()
	move = check(choice_list)
	for i in locations[current]:
		if i[0] == move:
			return i[1]

#function to show inventory
def show_inventory():
	print("Your inventory contains:")
	for i in inventory:
		print(f"- {i.title()}")

#function to check choices against the possible choices
def check_choice(choices, text):
	print(f'{text}Options:')
	num = 0
	for i in choices:
		print(f"- {choices[num]}")
		num += 1
	choice = input('\n').lower().strip()
	while choice not in choices:
		print('\nInvalid command\nOptions:')
		num = 0
		for i in choices:
			print(f"- {choices[num]}")
			num += 1
		choice = input('').lower().strip()
	return choice

def check(choices):
	choice = input("What is your choice?\n").lower().strip()
	while choice not in choices:
		print('\nInvalid command\nOptions:')
		num = 0
		for i in choices:
			print(f"- {choices[num]}")
			num += 1
		choice = input("What is your choice?\n").lower().strip()
	return choice

#Scenario for first time in cabin.
def cabin(started):
	if started == 0:
		print("You wake up in a cabin bed, you don't know how you got here.\nThe clock beside you reads 10:30 PM.\nYou look outside the window, there is a dark forest.\nYou can exit to the north.")
		choice = check_choice(["north", "stay"], "\nWhat do you want to do?\n")
		if choice == "north":
			print("\nYou go north and leave the cabin\nYou have entered the forest")
			started = 1
		else:
			print("\nYou stay in bed and wake up the next morning.\n")
	else:
		print("You are back at the cabin.")

#scenario for forest.
def forest_scenario():
	print()
	scenario = random.randint(1, 3)
	if scenario == 1:
		print("You hear a loud noise.\nYou look around but don't see anything.")
	elif scenario == 2:
		print("You notice how muddy the ground is.")
	elif scenario == 3:
		print("You are starting to feel hungry and consider going back to the cabin to find food.")
	else:
		print("You are in a different part of the forest")


#scenario for box of food.
def food(got_food):
	if got_food == 0:
		print("\nYou find a box in the forest.")
		choice = check_choice(["yes", "no"], "\nDo you want to open it?\n")
		if choice == "yes":
			print("\nYou open the box and find some food.")
			got_food = 1
			inventory.append("Food")
			show_inventory()
		else:
			print("\nYou decide not to open the box.")
	else:
		print("\nYou are back at the box where you found food")

#scenario for guard interaction.
def guard(guard_approached):
	if guard_approached == 0:
		print("\nYou see a guard standing in front of a large stone statue.")
		choice = check_choice(["yes", "no"], "\nDo you want to talk to the guard?\n")
		if choice == "yes":
			print("\nYou approach the guard.\nHe says he will move if you give him your food.")
			if "Food" in inventory:
				choice = check_choice(["yes", "no"], "\nDo you give the guard your food?\n")
				if choice == "yes":
					print("\nYou give the guard your food.\nHe disappears revealing a key in the stone.\nYou pick up the key.")
					inventory.remove("Food")
					inventory.append("Key")
					show_inventory()
				else:
					print("You refuse to give the guard your food.\nHe wishes you a good day.")
			else:
				print("You do not have any food.\nYou should keep looking.")
		else:
			print("You ignore the guard and leave that part of the forest.")
	else:
		print("You are back where you found the guard")
	
#scenario for hatch
def hatch(hatch_opened):	
	if hatch_opened == 0:
		print("\nYou come across a large concrete pad with two metal doors laying on it.")
		choice = check_choice(["yes", "no"], "\nDo you try to open the doors?\n")
		if choice == "yes":
			if "Key" in inventory:
				print("\nYou try to open the doors but notice a lock preventing them from being opened.")
				choice = check_choice(["yes", "no"], "\nDo you want to use your key?\n")
				if choice == "yes":
					print("\nYou use your key to unlock the doors\nWhen you open them, you see a ladder leading down into darkness.")
					inventory.remove("Key")
					hatch_opened = 1
					complete = True
					return complete
				else:
					print("You save your key for a lucky day.")
			else:
				print("It looks like you need to find a key.")
		else:
			print("You don't try to open the doors and you leave that part of the forest")

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


print("You wake up in a cabin bed, you don't know how you got here.\nThe clock beside you reads 10:30 PM.\nYou look outside the window, there is a dark forest.\nYou can exit to the north.\n")
choice = check_choice(["north", "stay"], "\nWhat do you want to do?\n")
if choice == "north":
	print("\nYou go north and leave the cabin\nYou have entered the forest")
	current = "f6"
else:
	print("\nYou stay in bed and wake up the next morning.")
	current = "cabin"
started = 1


complete = True


#main game loop
while complete != True:
	move = movement(current)
	if move == "food":
		food(got_food)
		current = move
	elif move == "cabin":
		cabin(started)
		current = move
	elif move == "key":
		guard(guard_approached)
		current = move
	elif move == "hatch":
		complete = hatch(hatch_opened)
		current = move
	else:
		forest_scenario()
		current = move

#Finish message
print('''
   _____                                  _           _         _    _                    
  / ____|                                | |         | |       | |  (_)                   
 | |      ___   _ __    __ _  _ __  __ _ | |_  _   _ | |  __ _ | |_  _   ___   _ __   ___ 
 | |     / _ \ | '_ \  / _` || '__|/ _` || __|| | | || | / _` || __|| | / _ \ | '_ \ / __|
 | |____| (_) || | | || (_| || |  | (_| || |_ | |_| || || (_| || |_ | || (_) || | | |\__ \ 
  \_____|\___/ |_| |_| \__, ||_|   \__,_| \__| \__,_||_| \__,_| \__||_| \___/ |_| |_||___/
                        __/ |                                                             
                       |___/                                                              
''')
print('''
		 __   __ ___   _   _  __        __ ___   _   _   _ 
		 \ \ / // _ \ | | | | \ \      / // _ \ | \ | | | |
		  \ V /| | | || | | |  \ \ /\ / /| | | ||  \| | | |
		   | | | |_| || |_| |   \ V  V / | |_| || |\  | |_|
		   |_|  \___/  \___/     \_/\_/   \___/ |_| \_| (_)
                                                   
''')