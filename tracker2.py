def readFile(claimFilename):
    """
    Open the file and read the content
    :param claimFilename: file
    :return: list
    """
    file = open(claimFilename, 'r')
    claimList = file.readlines()
    file.close()

    return claimList

def getInfo(claimList):
    """
    Process information about the claim file
    :param claimList: list
    :return: str
    """
    print("""
1. Claim Number
2. Flight Route
3. Claims Agent
4. Bag Description
    """)

    flightInfo = claimList[0].split("_") # first line of the file content
    claimNumber = flightInfo[1].strip() # part 2 of the first line of file content
    flightRoute = flightInfo[0].strip() # part 1 of the first line of file content

    claimsAgent = claimList[1].strip() # second line of file content
    bagDescription = claimList[2].strip() # third line of the file content

    userChoice = input("Enter the sno. of the detail: ")

    while not "1" <= userChoice <= "4":
        print("Invalid input. Try again: ")
        userChoice = input("Enter the sno. of the detail: ")

    information = " "

    if userChoice == "1":
        information = f"# Claim Number: {claimNumber}"
    elif userChoice == "2":
        information = f"# Flight Route: {flightRoute[:3]} -> {flightRoute[3:]}"
        # returns the first three letters and the last three letters
    elif userChoice == "3":
        information = f"# Claims Agent: {claimsAgent}"
    elif userChoice == "4":
        information = f"# Bag Description: {bagDescription}"

    return information, claimNumber

def getBags(claimNumber):
    """
    Generate a new file and create a unified list that contains the new info
    :param claimNumber: int
    :return: list
    """
    unifiedList = []
    for i in range(3):
        generateFileName = f"{claimNumber}bag{i+1}.txt"
        newFile = readFile(generateFileName)
        for line in newFile:
            unifiedList.append(line.strip())

    return unifiedList

def displayBags(unifiedList):
    """
    display the information of the new bags
    :param unifiedList:
    :return:
    """
    bagTag = []
    bagDescription = []
    for i in range(len(unifiedList)):
        if i % 2 == 0: # checks if index is even number
            bagTag.append(unifiedList[i])
        elif i % 2 == 1: # checks if index is odd number
            bagDescription.append(unifiedList[i])

    for i in range(3):
        print(f"# Bag {i+1}\n{bagTag[i]}\n{bagDescription[i]}")


def main():
    welcomeMessage = "<< Welcome to Claims Desk! >>"
    print(f"{'*' * len(welcomeMessage)}\n{welcomeMessage}\n{'*' * len(welcomeMessage)}")

    while True:
        claimFilename = input("Enter claim file name: ")

        claimList = readFile(claimFilename)

        information, claimNumber = getInfo(claimList)
        print(f"Here is the detail you requested about the claim\n{information}")

        unifiedList = getBags(claimNumber)

        storage = input("See bags in storage? (y/n): ")
        if storage == "y":
            displayBags(unifiedList)

        goAgain = input("Process another claim? (y/n): ").lower()

        if goAgain == "n":
            print("<< Claims Desk Session Closed >>")
            exit()

if __name__ == "__main__":
    main()