"""
Title: Arcade 3
Date: 09/22/2026
Author: Austin WP
"""

name = input("Enter your name: ")
name = name.title() # .title() method capitalizes the first letter of each word

favouriteColour = input("Enter your favourite colour: ")
favouriteColour = favouriteColour.title() # .title() method capitalizes the first letter of each word - very convenient! :)

welcomeMessage = f"Welcome to {favouriteColour} Arcade"

bannerLength = len(welcomeMessage)

print("*" * bannerLength) # string multiplication used to match banner with the length of the welcome message
print(welcomeMessage)
print("*" * bannerLength)

print(f"Hello {name}!")

favouriteGenre = input("Enter your favourite genre: ")
favouriteGenre = favouriteGenre.lower()

# string addition joins specific words into one string
specialCode = favouriteColour[0:2] + name[-1] + favouriteGenre[0:2] # [0:2] uses the first two letters in the string
specialCode = specialCode.upper() # .upper() method makes everything uppercase
print(f"Here is your special code for your next visit: '{specialCode}'")

balance = (((len(favouriteColour) + len(favouriteGenre))/2) + (len(name))/2)
print(f"Your balance: ${balance}0")

if favouriteGenre == "action":
    # Display Games
    print("""
    Available Games:
    Street Brawler - $7
    Laser Tag - $5
    """)

    # Attempt to Purchase
    if balance >= 7:
        print("Loaded up Street Brawler!")
        remainingBalance = balance - 7
        print(f"Remaining Balance: ${remainingBalance}0")
    elif 5 <= balance < 7:
        print("Loaded up Street Brawler!")
        remainingBalance = balance - 5
        print(f"Remaining Balance: ${remainingBalance}0")
    else:
        print("You cannot afford a game :(")
        print(f"Remaining Balance: ${balance}0")

elif favouriteGenre == "racing":
    # Display Games
    print("""
    Available Games:
    Turbo Drift - $6
    Moto GP - $5 
    """)

    # Attempt to Purchase
    if balance >= 6:
        print("Loaded up Turbo Drift!")
        remainingBalance = balance - 6
        print(f"Remaining Balance: ${remainingBalance}0")
    elif 5 <= balance < 6:
        print("Loaded up Moto GP!")
        remainingBalance = balance - 5
        print(f"Remaining Balance: ${remainingBalance}0")
    else:
        print("You cannot afford a game :(")
        print(f"Remaining Balance: ${balance}0")

elif favouriteGenre == "shooter":
    # Display Games
    print("""
    Available Games:
    Galaxy Wars - $8
    Duck Hunt - $6
    """)

    # Attempt to Purchase
    if balance >= 8:
        print("Loaded up Galaxy Wars!")
        remainingBalance = balance - 8
        print(f"Remaining Balance: ${remainingBalance}0")
    elif 6 <= balance < 8:
        print("Loaded up Duck Hunt!")
        remainingBalance = balance - 6
        print(f"Remaining Balance: ${remainingBalance}0")
    else:
        print("You cannot afford a game :(")
        print(f"Remaining Balance: ${balance}0")

elif favouriteGenre == "puzzle":
    # Display Games
    print("""
    Available Games:
    Block Drop - $10
    Maze Runner - $5
    """)

    # Attempt to Purchase
    if balance >= 10:
        print("Loaded up Block Drop!")
        remainingBalance = balance - 10
        print(f"Remaining Balance: ${remainingBalance}0")
    elif 5 <= balance < 10:
        print("Loaded up Maze Runner!")
        remainingBalance = balance - 5
        print(f"Remaining Balance: ${remainingBalance}0")
    else:
        print("You cannot afford a game :(")
        print(f"Remaining Balance: ${balance}0")
else:
    print(f"There are no games for the {favouriteGenre} genre.")

