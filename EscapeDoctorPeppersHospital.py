def show_instructions():
    # Prints main menu and commands
    print(" ___________________________________________________________________________________ ")
    print("|                                   Main Menu                                       |")
    print("| --------------------------------------------------------------------------------- |")
    print("| Escape from Doctor Pepper's Hospital - Text Adventure Game                        |")
    print("| Collect 8 items to face Dr.Pepper, get his gas mask, and escape or die trying.    |")
    print("| Move commands: go South, go North, go East, go West                               |")
    print("| Add to Inventory: get [item name]                                                 |")
    print("|___________________________________________________________________________________|")
    print()  # Add space at the end of instructions


def command_actions(command, current_room, rooms, items, inventory):
    # Function to handle the commands (go <direction> or get <item>)
    if command.startswith('get '):
        item_to_get = command[4:]
        # Check if the item is available in the current room
        if item_to_get in items and items[item_to_get] == current_room:
            inventory.append(item_to_get)
            print(f"\nYou have acquired a {item_to_get}")
            del items[item_to_get]
        else:
            print(f"{item_to_get} is not available in this room.")

    elif command.startswith('go '):
        direction = command[3:].capitalize()
        # Check if the direction is valid for the current room
        if direction in rooms[current_room]:
            # Move to the new room
            current_room = rooms[current_room][direction]  
        else:
            print("There's no door there, try another direction.")
    return current_room

def main():
    rooms = {
        "Dr.Peppers Office": {"East": "Security Room"},
        "Main Lobby": {"East": "Vending Machine Area", "North": "Break Room"},
        "Break Room": {"South": "Main Lobby"},
        "Vending Machine Area": {"West": "Main Lobby", "North": "Medical Supply Room", "East": "Reception Area", "South": "Security Room"},
        "Reception Area": {"West": "Vending Machine Area"},
        "Medical Supply Room": {"South": "Vending Machine Area", "East": "Administrative Room"},
        "Administrative Room": {"West": "Medical Supply Room", "East": "Maintenance Room"},
        "Maintenance Room": {"West": "Administrative Room"},
        "Security Room": {"West": "Dr.Peppers Office", "East": "Janitors Closet", "North": "Vending Machine Area"},
        "Janitors Closet": {"West": "Security Room"}
    }

    items = {
        'Bandage': 'Medical Supply Room',
        'Key': 'Administrative Room',
        'Flashbang': 'Security Room',
        'Map': 'Reception Area',
        'Research Note': 'Janitors Closet',
        'Protein Bar': 'Vending Machine Area',
        'Water Bottle': 'Break Room',
        'Pocket Knife': 'Maintenance Room'
    }

    inventory = []
    current_room = "Main Lobby"

    while current_room != "Exit":
        print(f"\nYou are in the {current_room}")
        print(f"Inventory: {inventory}")
        print("-------------------------")

        if current_room in items.values():
            print("You see a", ", ".join([item for item, room in items.items() if room == current_room]))

        command = input("Enter your move: ")

        if command == "exit":
            current_room = "Exit"
            print("Thanks for playing!")
            break

        current_room = command_actions(command, current_room, rooms, items, inventory)

        if current_room == "Dr.Peppers Office": # Validates if player has all 8 items when entering Dr.Peppers office
            if len(inventory) == 8: 
              # If player has all 8 items, they win
                print("\nCongratulations! You have collected all items and stunned Dr.Pepper to take his High Tech Mask")
                print("Thanks for playing the game. Hope you enjoyed it.")
                break
            else: 
              # If player had less than 8 items, they lose
                print("\nDR.PEPPER RELEASED A GAS CANISTER AND YOU SUFFOCATED ... GAME OVER!")
                print("Thanks for playing the game. Hope you enjoyed it.")
                break

# Start the game
show_instructions()
main()
