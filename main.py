from start import *

print(first_cabin)
choice = input(fcabin_choice)
while choice != fcabin_choice_opt[1]:
	if choice not in fcabin_choice_opt:
		print(f'\nInvalid command\nOptions: "{fcabin_choice_opt[0]}" or "{fcabin_choice_opt[1]}"\n')
	else:
		print(fcabin_stay)
	choice = input(fcabin_choice)
print(fcabin_leave)