def readKitchen(filename):
    """
    reads the file and builds a 2D kitchen map
    :param filename: .txt file
    :return: 2D list
    """
    grid = []

    with open(filename, "r") as file:
        content = file.readlines()
        for line in content:
            row = []
            cleanLine = line.strip()

            for letter in cleanLine:
                row.append(letter)

            grid.append(row)

    return grid

def getIcon(char):
    """
    gets the corresponding emoji icon associated with the character
    :param char: str
    :return: str
    """
    char = char.lower()
    emoji = ""
    icons = (('c', '👨'), ('*', '⬜'), ('e', '📟'), ('o', '🔔'), ('s', '🔥'), ('f', '🍳'), ('w', '🧊'))

    for item in icons:
        if char == item[0]:
            emoji = item[1]

    return emoji

def displayKitchen(kitchenMap):
    """
    displays the kitchen map with emojis that represent the kitchen
    :param kitchenMap: 2D list
    :return:
    """
    for row in kitchenMap:
        for char in row:
            print(getIcon(char), end=" ")
        print()

def findChef(kitchenMap):
    """
    locate the chef's position
    :param kitchenMap: 2D list
    :return: tuple
    """
    chefPosition = ""
    for i in range(len(kitchenMap)):
        for j in range(len(kitchenMap[i])):
            if kitchenMap[i][j] == "C":
                chefPosition = (i, j)

    return chefPosition


def main():
    filename = input("Enter filename: ")
    kitchenMap = readKitchen(filename)
    print(kitchenMap)
    displayKitchen(kitchenMap)
    chef = findChef(kitchenMap)
    print(f"Chef is at: {chef}")


if __name__ == "__main__":
    main()
