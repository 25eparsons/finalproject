from start import *

print(first_cabin)
choice = input(fcabin_choice)
while choice != fcabin_choice_opt[1]:
	if choice not in fcabin_choice_opt:
		print(f"\nInvalid command\nUse {fcabin_choice_opt}")
	else:
		print(fcabin_stay)
	choice = input(fcabin_choice)
print(fcabin_leave)