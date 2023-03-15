locations = {
"cabin": [["north", "f6"], ["south", "random"]]
}

def check_choice(choices):
	choice = input("What is your choice?\n").lower().strip()
	while choice not in choices:
		print(f'\nInvalid command\nOptions: "{choices[0]}" or "{choices[1]}"')
		choice = input("What is your choice?\n").lower().strip()
	return choice

def movement(current):
	print("You can move:")
	num = 0
	choice_list = []
	for i in locations[current]:
		moves = locations.get(current)[num][0]
		choice_list.append(moves)
		print("- " + moves)
		num += 1
	
	move = check_choice(choice_list)
	moved_to = locations[cabin["move"]]
	print(moved_to)

new_space = movement("cabin")
print(new_space)