import sys

snack_inventory = []


def add_snack():
    snack_id = input("Enter the snack ID: ")
    snack_name = input("Enter the snack name: ")
    snack_price = float(input("Enter the snack price: "))
    snack_availability = input("Is the snack available? (yes/no): ")

    snack = {
        "id": snack_id,
        "name": snack_name,
        "price": snack_price,
        "availability": snack_availability.lower() == "yes",
    }

    snack_inventory.append(snack)
    print()
    print("Snack added successfully!")


def remove_snack():
    snack_id = input("Enter the snack ID: ")

    for snack in snack_inventory:
        if snack["id"] == snack_id:
            snack_inventory.remove(snack)
            print()
            print("Snack removed successfully!")
            return
    print()
    print("Snack not found.")


def update_availability():
    snack_id = input("Enter the snack ID: ")

    for snack in snack_inventory:
        if snack["id"] == snack_id:
            snack_availability = input("Is the snack available? (yes/no): ")
            snack["availability"] = snack_availability.lower() == "yes"
            print()
            print("Snack updated successfully!")
            return

    print()
    print("Snack not found.")


def sell_snack():
    snack_id = input("Enter the snack ID: ")

    for snack in snack_inventory:
        if snack["id"] == snack_id:
            if snack["availability"]:
                print()
                print(f"Snack {snack_id} sold successfully!")
                snack["availability"] = False
            else:
                print()
                print("Snack not available.")
            return

    print()
    print("Snack not found in the inventory.")


def list_all_snacks():
    print("Snack Inventory:")
    print()

    if len(snack_inventory) == 0:
        print("No snacks available.")
    else:
        for snack in snack_inventory:
            availability = "Available" if snack["availability"] else "Not Available"
            print(
                f"ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}, Availability: {availability}"
            )


def show_menu():
    print()
    print("Welcome to Mumbai Munchies: The Canteen Chronicle!")
    print("1. Add a snack")
    print("2. Remove a snack")
    print("3. Update snack availability")
    print("4. Sell a snack")
    print("5. List all snacks")
    print("6. Exit")
    print()


def get_user_choice():
    choice = input("Enter your choice (1-6): ")
    print()
    return choice


def handle_user_choice(choice):
    if choice == "1":
        add_snack()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_availability()
    elif choice == "4":
        sell_snack()
    elif choice == "5":
        list_all_snacks()
    elif choice == "6":
        print("Thank you for using Mumbai Munchies: The Canteen Chronicle!")
        sys.exit()
    else:
        print()
        print("Invalid choice. Please try again.")


while True:
    show_menu()
    user_choice = get_user_choice()
    handle_user_choice(user_choice)
