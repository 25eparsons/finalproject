import random

from text import *

print("Welcome to my game!")
print(instructions)
playername = input("What do you want you name to be?\n")
print(f"\nGood luck {playername},")
input(game_name)
print("\n\n\n")

#Scenario for first time in cabin.
print(first_cabin)
choice = input(fcabin_choice)
while choice != fcabin_choice_opt[1]:
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