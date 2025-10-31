
slots = [0] * 20

def display():
	print("Parking Status:")
	print(f"Total Slots: {len(slots)}")
	print(f"Available: {slots.count(0)}")
	print(f"Occupied: {slots.count(1)}")

def park_car():
	for i in range(len(slots)):
		if slots[i] == 0:
			slots[i] = 1
			print(f" Car parked in slot {i + 1}")
			return
			print(" Parking lot is full!")

def remove_car():
	slot_num = int(input("Enter slot number to remove car (1-20): "))
	if 1 <= slot_num <= 20:
		if slots[slot_num - 1] == 1:
			slots[slot_num - 1] = 0
			print(f" Car removed from slot {slot_num}")
		else:	
			print(" Slot is already empty.")
       
while True:
    print("Choose an action:")
    print("1. Park a car")
    print("2. Remove a car")
    print("3. Display status")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        park_car()
    elif choice == "2":
        remove_car()
    elif choice == "3":
        display_status()
    elif choice == "4":
        print(" Exiting...")
        break
    else:
        print(" Invalid choice. Try again.")

