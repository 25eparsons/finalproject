import random

from text import *

input(instructions)
print(commands)
playername = input("What do you want your name to be?\n")
print(f"\nGood luck {playername},")
input(game_name)
print("\n\n\n")

#Scenario for first time in cabin.
choice = input(first_cabin)
while choice != fcabin_choice_opt[0]:
	if choice not in fcabin_choice_opt:
		print(f'\nInvalid command\nOptions: "{fcabin_choice_opt[0]}" or "{fcabin_choice_opt[1]}"\n')
	else:
		print(fcabin_stay)
	choice = input(fcabin_choice)
print(fcabin_leave)

#scenario for forest.
scenario = random.randint(1, 3)
if scenario == 1:
	print(forest_noise)
elif scenario == 2:
	print(forest_mud)
elif scenario == 3:
	print(forest_hunger)

#scenario for box of food.
print(forest_food)
choice = input(food_choice)
while choice not in food_choice_opt:
	print(f'\nInvalid command\nOptions: "{food_choice_opt[0]}" or "{food_choice_opt[1]}"')
	choice = input(food_choice)
if choice == food_choice_opt[0]:
	print(food_open)
	inventory.append(food_item)
	print(f"Your inventory now contains {inventory}.")
else:
	print(food_leave)

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
			print(f"Your inventory now contains {inventory}.")
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
			
