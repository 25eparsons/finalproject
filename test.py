from text import *
print(forest_guard)
choice = input(guard_choice)
while choice not in guard_choice_opt:
	print(f'\nInvalid command\nOptions: "{guard_choice_opt[0]}" or "{guard_choice_opt[1]}"\n')
	choice = input(guard_choice)
if choice == guard_choice_opt[0]:
    print(guard_approach)
    guard_choice = input(guard_approach_choice)
    while guard_choice not in guard_approach_choice_opt:
        print(f'\nInvalid command\nOptions: "{guard_approach_choice_opt[0]}" or "{guard_approach_choice_opt[1]}"\n')
        choice = input(guard_approach_choice)
    if guard_choice == guard_approach_choice_opt[0]:
        print(guard_approach_give)
        inventory.append(key_item)
    else:
        print(guard_approach_refuse)
else:
    print(guard_ignore)