def checkUsername(username, domainList):
    """
    Checks if username has a single @ sign and is in the domainList
    :param username: str
    :param domainList: list
    :return: bool
    """
    validUsername = False

    if username.count("@") == 1:
        name, domain = username.split("@")
        if domain in domainList:
            validUsername = True
            print("Valid username")
    else:
        print("Invalid username")

    return validUsername


def verifyPassword(password):
    verification = False
    verifyPassword = input("Please enter your password again: ")

    if verifyPassword == password:
        verification = True

    return verification

def main():
    username = input("Enter your email address: ")
    domainList = ["ualberta.ca", "gmail.com"]
    validUsername = checkUsername(username, domainList)

    if validUsername:
        password = input("Enter your password: ")
        verification = verifyPassword(password)
        if verification:
            print("Valid password")



if __name__ == "__main__":
    main()