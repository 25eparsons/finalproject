instructions= "Here are the instructions:\n"

game_name = '''Welcome to

 _____  _             _____                       _   
|_   _|| |__    ___  |  ___|___   _ __  ___  ___ | |_ 
  | |  | '_ \  / _ \ | |_  / _ \ | '__|/ _ \/ __|| __|
  | |  | | | ||  __/ |  _|| (_) || |  |  __/\__ \| |_ 
  |_|  |_| |_| \___| |_|   \___/ |_|   \___||___/ \__|
		(Press enter to begin)\n'''

inventory = []

first_cabin = "You wake up in a cabin bed, you don't know how you got here.\nThe clock beside you reads 10:30 PM.\nYou look outside the window, there is a dark forest.\n"
fcabin_choice = "Do you choose to leave the cabin?\n"
fcabin_choice_opt = ["yes", "no"]
fcabin_stay = "\nYou go to bed and wake up the next morning.\n"
fcabin_leave = "\nYou leave the cabin and find yourself in the forest."

cabin = "You are back at the cabin"


forest = "You are in a different part of the forest"

forest_noise = "You hear a loud noise.\nYou look around but don't see anything."

forest_mud = "You notice how muddy the ground is."

forest_hunger = "You are starting to feel hungry and consider going back to the cabin to find food."

forest_food = "\nYou find a box in the forest."
food_choice = "\nDo you choose to open the box?\n"
food_choice_opt = ["yes", "no"]
food_open = "\nYou open the box and find some food."
food_item = "food"
food_leave = "\nYou decide not to open the box."

forest_guard = "You see a guard standing in front of a large stone statue.\n"
guard_choice = "Do you choose to approach the guard?\n"
guard_choice_opt = ["yes", "no"]
guard_approach = "\nYou approach the guard.\nHe says he will move if you give him your food."
guard_approach_nofood = "You do not have any food.\nYou should keep looking."
guard_approach_choice = "\nDo you give the guard food?\n"
guard_approach_choice_opt = ["yes", "no"]
guard_approach_give = "\nYou give the guard your food.\nHe moves aside revealing a key in the stone.\nYou pick up the key."
key_item = "key"
guard_approach_refuse = "You refuse to give the guard your food.\nHe wishes you a good day."
guard_ignore = "You ignore the guard and leave that part of the forest."

forest_hatch = "\nYou come across a large concrete pad with two metal doors laying on it."
hatch_choice = "\nDo you try to open the doors?\n"
hatch_choice_opt = ["yes", "no"]
hatch_open = "\nYou try to open the doors but notice a lock preventing them from being opened."
hatch_open_keychoice = "Do you want to use your key?\n"
keychoice_opt = ["yes", "no"]
hatch_open_yes = "\nYou use your key to unlock the doors\nWhen you open them, you see a ladder leading down into darkness.\nWhat do you choose to do?"
hatch_open_no = "You save your key for a lucky day."
hatch_open_nokey = "It looks like you need to find a key."
hatch_leave = "You don't try to open the doors and you leave that part of the forest"

ladder_choice = "Climb down the ladder or leave and come back later?"
ladder_down = "You begin to climb down the ladder.\nIt is starting to get very dark."
ladder_leave = "You leave the area of the forest with the ladder."

fail_msg = "You have died"