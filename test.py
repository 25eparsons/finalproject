locations = {
"cabin": [["north", "f6"], ["south", "random"],["west", "house"]]
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
	print()
	move = check_choice(choice_list)
	for i in locations[current]:
		if i[0] == move:
			return i[1]
	

new_space = movement("cabin")
print(new_space)