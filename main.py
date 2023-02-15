#intro cabin text
cabinintro = "You wake up in a cabin bed, you don't know how you got here.\nThe clock beside you reads 10:30 PM.\nYou look outside the window, there is a dark forest.\n\nOptions:"
print(cabinintro)
choice = ""
while choice != "leave":
	choice = input("Leave the cabin or stay until morning?\n")
	if choice == "stay":
		print("You wake back up in the cabin")
		print(f"It is now 8:15 AM")
	elif choice != "leave" or choice != "stay":
		print("-improper input message-")


#forest message
print("You are now in the forest")
print("Options:")
choice = input("")

print("You're back in the cabin")
# cabin text