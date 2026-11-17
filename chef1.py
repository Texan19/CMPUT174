def readKitchen(filename):
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
    char = char.lower()
    emoji = ""
    icons = (('c', '👨'), ('*', '⬜'), ('e', '📟'), ('o', '🔔'), ('s', '🔥'), ('f', '🍳'), ('w', '🧊'))

    for item in icons:
        if char == item[0]:
            emoji = item[1]

    return emoji

def displayKitchen(kitchenMap):
    for row in kitchenMap:
        for char in row:
            print(getIcon(char), end=" ")
        print()

def findChef(kitchenMap):
    chefPosition = ""
    for i in range(len(kitchenMap)):
        for j in range(len(kitchenMap[i])):
            if kitchenMap[i][j] == "C":
                chefPosition = (i, j)

    print(f"Chef is at {chefPosition}")

def main():
    filename = input("Enter filename: ")
    kitchenMap = readKitchen(filename)
    print(kitchenMap)
    emoji = getIcon('C')
    displayKitchen(kitchenMap)
    findChef(kitchenMap)

if __name__ == "__main__":
    main()
