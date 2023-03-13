from text import *

def check_choice(choices):
	choice = input("What is your choice?\n").lower().strip()
	while choice not in choices:
		print(f'\nInvalid command\nOptions: "{choices[0]}" or "{choices[1]}"')
		choice = input("What is your choice?\n").lower().strip()
	return choice

choice = check_choice(food_choice_opt)
print(choice)