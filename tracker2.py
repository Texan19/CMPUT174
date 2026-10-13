def readFile(claimFilename):
    """
    Open the file and read the content
    :param claimFilename: file
    :return: list
    """

    file = open(claimFilename, 'r')
    fileContent = file.readlines()
    file.close()

    return fileContent

def getInfo(fileContent):
    """
    Process information about the claim file
    :param fileContent: list
    :return: str
    """

    print("""
1. Claim Number
2. Flight Route
3. Claims Agent
4. Bag Description
    """)

    flightInfo = fileContent[0].split("_") # first line of the file content
    claimNumber = flightInfo[1].strip() # part 2 of the first line of file content
    flightRoute = flightInfo[0].strip() # part 1 of the first line of file content

    claimsAgent = fileContent[1].strip() # second line of file content
    bagDescription = fileContent[2].strip() # third line of the file content

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
    unifiedList = []
    for i in range(3):
        generateFileName = f"{claimNumber}bag{i+1}.txt"
        newFile = readFile(generateFileName)
        for line in newFile:
            line.strip().split(",")
            unifiedList.append(line)

    return unifiedList

def displayBags(unifiedList):
    storage = input("See bags in storage? (y/n): ").lower()
    if storage == "y":
        pass

def main():
    welcomeMessage = "<< Welcome to Claims Desk! >>"
    print(f"{'*' * len(welcomeMessage)}\n{welcomeMessage}\n{'*' * len(welcomeMessage)}")

    while True:
        claimFilename = input("Enter claim file name: ")

        fileContent = readFile(claimFilename)

        information, claimNumber = getInfo(fileContent)
        print(f"Here is the detail you requested about the claim\n{information}")

        unifiedList = getBags(claimNumber)

        displayBags(unifiedList)

        goAgain = input("Process another claim? (y/n): ").lower()

        if goAgain == "n":
            print("Claims Desk Session Closed")
            exit()

if __name__ == "__main__":
    main()