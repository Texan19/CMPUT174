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
    claimNumber = flightInfo[1] # part 2 of the first line of file content
    flightRoute = flightInfo[0] # part 1 of the first line of file content

    claimsAgent = claimList[1] # second line of file content
    bagDescription = claimList[2] # third line of the file content

    userChoice = input("Enter the sno. of the detail: ")

    while not "1" <= userChoice <= "4":
        print("Invalid input. Try again: ")
        userChoice = input("Enter the sno. of the detail: ")

    if userChoice == "1":
        return f"# Claim Number: {claimNumber}"
    elif userChoice == "2":
        return f"# Flight Route: {flightRoute[:3]} -> {flightRoute[3:]}"
        # returns the first three letters and the last three letters
    elif userChoice == "3":
        return f"# Claims Agent: {claimsAgent}"
    elif userChoice == "4":
        return f"# Bag Description: {bagDescription}"

def main():
    welcomeMessage = "<< Welcome to Claims Desk! >>"
    print(f"{'*' * len(welcomeMessage)}\n{welcomeMessage}\n{'*' * len(welcomeMessage)}")

    while True:
        claimFilename = input("Enter claim file name: ")

        claimList = readFile(claimFilename)

        information = getInfo(claimList)
        print(f"Here is the detail you requested about the claim\n{information}")

        goAgain = input("Process another claim? (y/n): ").lower()

        if goAgain == "n":
            print("Claims Desk Session Closed")
            exit()

if __name__ == "__main__":
    main()