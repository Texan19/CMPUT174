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


def locateOrderStation(kitchenMap):
    """
    locate the order station's position
    :param kitchenMap: 2D list
    :return: tuple
    """
    orderPosition = ""
    for i in range(len(kitchenMap)):
        for j in range(len(kitchenMap[i])):
            if kitchenMap[i][j] == "O":
                orderPosition = (i, j)

    return orderPosition

def locatePickupCounter(kitchenMap):
    """
    locate the pickup station's position
    :param kitchenMap: 2D list
    :return: tuple or None
    """
    for i in range(len(kitchenMap)):
        for j in range(len(kitchenMap[i])):
            if kitchenMap[i][j] == "E":
                pickupPosition = (i, j)
                return pickupPosition
    return None

def getValidMoves(kitchenMap, chefPosition):
    """
    check if the chef can move one tile up, down, left, right
    :param kitchenMap: 2D list
    :param chefPosition: tuple
    :return: 2D tuple
    """
    validMoves = []
    validPositions = ("*", "E", "O")

    chefRow = chefPosition[0]
    chefCol = chefPosition[1]

    # 1. UP
    if chefRow - 1 >= 0 and kitchenMap[chefRow - 1][chefCol] in validPositions: # Check up: Verify index is in bounds first, then check the tile character
        validMoves.append((chefRow - 1 , chefCol))

    # 2. DOWN
    if chefRow + 1 < len(kitchenMap) and kitchenMap[chefRow + 1][chefCol] in validPositions:
        # Check down: Verify index is in bounds first, then check the tile character
        validMoves.append((chefRow + 1, chefCol))

    # 3. LEFT
    if chefCol - 1 >=0 and kitchenMap[chefRow][chefCol - 1] in validPositions:
        # Check left: Verify index is in bounds first, then check the tile character
        validMoves.append((chefRow, chefCol - 1))

    # 4. RIGHT
    if chefCol + 1 < len(kitchenMap[0]) and kitchenMap[chefRow][chefCol + 1] in validPositions:
        # Check right: Verify index is in bounds first, then check the tile character
        validMoves.append((chefRow, chefCol + 1))


    return validMoves


def main():
    filename = input("Enter filename: ")
    kitchenMap = readKitchen(filename)
    print(kitchenMap)
    displayKitchen(kitchenMap)

    chefPosition = findChef(kitchenMap)
    orderPosition = locateOrderStation(kitchenMap)
    pickupPosition = locatePickupCounter(kitchenMap)
    validMoves = getValidMoves(kitchenMap, chefPosition)

    print(f"Chef is at {chefPosition}")
    print(f"Order station is at {orderPosition}")
    print(f"Pickup station is at {pickupPosition}")
    print(f"Valid moves: {validMoves}")

if __name__ == "__main__":
    main()
