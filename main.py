#intro cabin text
import random
time = random.randint(10,59)
print("You wake up in a cabin bed, you don't know how you got here.")
print(f"The clock beside you reads 10:{time} PM.")
print("You look outside the window, there is a dark forest.")
print("\nOptions:")
choice = ""
while choice != "leave":
	choice = input("Leave the cabin or stay until morning?\n")
	if choice == "stay":
		time = random.randint(10,59)
		print("You wake back up in the cabin")
		print(f"It is now 8:{time} AM")
	elif choice != "leave" or choice != "stay":
		print("-improper input message-")
print("-forest message-")

print("You're back in the cabin")
# cabin text