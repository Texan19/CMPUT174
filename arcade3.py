"""
Title: Arcade 3
Date: 09/22/2026
Author: Austin WP
"""

name = input("Enter your name: ").title() # .title() method capitalizes the first letter of each word

favouriteColour = input("Enter your favourite colour: ").title() # .title() method capitalizes the first letter of each word - very convenient! :)

welcomeMessage = f"Welcome to {favouriteColour} Arcade"

bannerLength = len(welcomeMessage)

print("*" * bannerLength) # string multiplication used to match banner with the length of the welcome message
print(welcomeMessage)
print("*" * bannerLength)

print(f"Hello {name}!")

favouriteGenre = input("Enter your favourite genre: ").lower() # .lower() method makes everything lowercase

# string addition joins specific words into one string
specialCode = (favouriteColour[:2] + name[-1] + favouriteGenre[:2]).upper()
# [:2] uses the first two letters in the string
# .upper() method makes everything uppercase
print(f"Here is your special code for your next visit: '{specialCode}'")

balance = (((len(favouriteColour) + len(favouriteGenre))/2) + (len(name))/2)
print(f"Your balance: ${balance:.2f}") #:.2f just formats the float to go to two decimal points

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
        balance -= 7
    elif balance >=5:
        print("Loaded up Street Brawler!")
        balance -= 5
    else:
        print("You cannot afford a game :(")

    print(f"Remaining Balance: ${balance:.2f}")

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
        balance -= 6
    elif balance >= 5:
        print("Loaded up Moto GP!")
        balance -= 5
    else:
        print("You cannot afford a game :(")

    print(f"Remaining Balance: ${balance:.2f}")

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
        balance -= 8
    elif balance >= 6:
        print("Loaded up Duck Hunt!")
        balance -= 6
    else:
        print("You cannot afford a game :(")

    print(f"Remaining Balance: ${balance:.2f}")

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
        balance -= 10
    elif balance >= 5:
        print("Loaded up Maze Runner!")
        balance -= 5
    else:
        print("You cannot afford a game :(")

    print(f"Remaining Balance: ${balance:.2f}")
else:
    print(f"There are no games for the {favouriteGenre} genre.")

