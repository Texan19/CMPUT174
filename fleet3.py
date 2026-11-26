def read_ships(filename):
    """
    reads a file and returns a dictionary of ships and their info
    :param filename: file object
    :return: dictionary
    """
    fleet = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip().split(",")
            ship_name = line[0]
            ship_class = line[1]
            ship_pwr = float(line[2])
            ship_rank = line[3]

            fleet[ship_name] = [ship_class, ship_pwr, ship_rank]

    return fleet

def display_ships(fleet):
    """
    displays the dictionary of ships and their info
    :param fleet: dictionary
    :return:
    """
    for ship, info in fleet.items():
        print(f"{ship:<16} CLASS: {info[0]} - PWR: {info[1]} - RANK: {info[2]}")

def add_ship(fleet):
    """
    adds a new ship to the fleet
    :param fleet: dictionary
    :return: str
    """
    new_ship = input("Enter name: ")
    if new_ship in fleet:
        return f"{new_ship} already exists"

    else:
        new_class = input("Enter class: ")
        new_pwr = float(input("Enter rank: "))
        new_rank = input("Enter rank: ")

        fleet[new_ship] = [new_class, new_pwr, new_rank]
        print(fleet[new_ship][1])
        return f"{new_ship} has been added!"

def remove_ship(fleet):
    """
    removes a ship from the fleet
    :param fleet: dictionary
    :return: str
    """
    delete_ship = input("Enter name: ")
    if delete_ship not in fleet:
        return f"{delete_ship} does not exist"
    else:
        fleet.pop(delete_ship)
        return f"{delete_ship} has been removed"

def recharge_ship(fleet):
    """
    updates the ship charge with a value that represents the percentage it is charged by
    :param fleet: dictionary
    :return: str
    """
    charge_ship = input("Enter name: ")
    if charge_ship not in fleet:
        return f"{charge_ship} does not exist"
    else:
        charge_percentage = int(input("Enter a ship charge: "))
        charge_percentage = (charge_percentage / 100) + 1
        current_power = fleet[charge_ship][1]
        new_power = (charge_percentage * current_power)
        fleet[charge_ship][1] = new_power
        new_power = round(new_power, 1)
        return f"{charge_ship}'s power is now {new_power}!"

def do_expeditions(fleet):
    expeditions = {
        "Scan": (23.4, "Beginner"),
        "Salvage": (55.1, "Intermediate"),
        "Warp": (68.4, "Advanced"),
        "Terraform": (78.9, "Expert")
    }

    print("EXPEDITIONS")
    for expedition, requirements in expeditions.items():
        print(f"\t- {expedition}: {requirements[0]} {requirements[1]}")

    mission = input("Enter mission: ")
    while mission not in expeditions:
        print(f"Expedition {mission} does not exist")
        mission = input("Enter mission: ")

    qualified = []

    for ship, item in fleet.items():
        if item[1] >= expeditions[mission][0] and item[2] == expeditions[mission][1]:
            qualified.append(ship)

    if len(qualified) == 0:
        print(f"Expedition {mission} is impossible")
    else:
        print(f"Qualified ships: {qualified}")



def main():
    filename = input("Enter file name: ")
    fleet = read_ships(filename)

    while True:
        print("\nMENU\n1. Display Ships\n2. Add Ship\n3. Remove Ship\n4. Recharge Ship\n5. Send on Expedition\n6. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            display_ships(fleet)
        elif choice == '2':
            print(add_ship(fleet))
        elif choice == '3':
            print(remove_ship(fleet))
        elif choice == '4':
            print(recharge_ship(fleet))
        elif choice == '5':
            do_expeditions(fleet)
        elif choice == '6':
            print("Safe travels, pilot!")
            return
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
