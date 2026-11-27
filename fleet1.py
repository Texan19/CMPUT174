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

def main():
    filename = input("Enter a filename: ")
    fleet = read_ships(filename)
    while True:
        print("\nMENU\n1. Display ships\n2. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            display_ships(fleet)
        elif choice == '2':
            print("Safe travels, pilot!")
            return
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
