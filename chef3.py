# - GLOBAL VARIABLES - #
POSSIBLE_MOVES = ["up", "down", "left", "right"]

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
    pos = ""
    for i in range(len(kitchenMap)):
        for j in range(len(kitchenMap[i])):
            if kitchenMap[i][j] == "C":
                pos = (i, j)

    return pos


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

def getValidMoves(kitchenMap, pos):
    """
    check if the chef can move one tile up, down, left, right
    :param kitchenMap: 2D list
    :param pos: tuple
    :return: 2D tuple
    """
    validMoves = []
    validPositions = ("*", "E", "O")

    chefRow = pos[0]
    chefCol = pos[1]

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

def getMove(validMoves, pos):
    """
    returns the new position of the chef depending on the direction chosen
    :param validMoves: 2D tuple
    :param pos: tuple
    :return: tuple
    """
    chefRow = pos[0]
    chefCol = pos[1]
    convertedMove = ()

    while True:
        direction = input("Enter move: ").lower().strip()

        if direction in POSSIBLE_MOVES:

            if direction == "up":
                convertedMove = (chefRow - 1, chefCol)
            elif direction == "down":
                convertedMove = (chefRow + 1, chefCol)
            elif direction == "left":
                convertedMove = (chefRow, chefCol - 1)
            elif direction == "right":
                convertedMove = (chefRow, chefCol + 1)

            if convertedMove in validMoves:
                return convertedMove


def moveChef(kitchenMap, pos, convertedMove, hasOrder):
    """
    move the chef and update the kitchen map depending on the chef's location
    :param kitchenMap: 2D list
    :param pos: tuple
    :param convertedMove: tuple
    :param hasOrder: bool
    :return: bool
    """
    convertedRow = convertedMove[0]
    convertedCol = convertedMove[1]
    chefRow = pos[0]
    chefCol = pos[1]


    if kitchenMap[convertedRow][convertedCol] == "E" and not hasOrder:
        return False
    else:
        kitchenMap[convertedRow][convertedCol] = "C"
        kitchenMap[chefRow][chefCol] = "*"
        return True


def main():
    filename = input("Enter filename: ")
    kitchenMap = readKitchen(filename)
    displayKitchen(kitchenMap)

    pos = findChef(kitchenMap)
    orderPosition = locateOrderStation(kitchenMap)
    pickupPosition = locatePickupCounter(kitchenMap)

    if pickupPosition is None:
        print("Critical: kitchen-map shows zero counters!")
        return

    hasOrder = False

    # - GAME LOOP - #
    while not (pos == pickupPosition and hasOrder):
        validMoves = getValidMoves(kitchenMap, pos)
        convertedMove = getMove(validMoves, pos)
        while not moveChef(kitchenMap, pos, convertedMove, hasOrder):
            convertedMove = getMove(validMoves, pos)

        displayKitchen(kitchenMap)
        pos = findChef(kitchenMap)

        if pos == orderPosition and not hasOrder:
            print("Order collected! 🔔")
            hasOrder = True

        if pos == pickupPosition and hasOrder:
            print("Service! Dish is out! 🍽️")



if __name__ == "__main__":
    main()
