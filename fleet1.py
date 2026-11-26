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
            fleet[line[0]] = line[1:]

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
    filename = input("Enter file name: ")
    fleet = read_ships(filename)
    while True:
        print("MENU\n1. Display Ships\n2. Exit")
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
