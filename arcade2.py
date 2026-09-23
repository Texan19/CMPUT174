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

elif favouriteGenre == "racing":
    # Display Games
    print("""
Available Games:
Turbo Drift - $6
Moto GP - $5 
    """)

elif favouriteGenre == "shooter":
    # Display Games
    print("""
Available Games:
Galaxy Wars - $8
Duck Hunt - $6
    """)

elif favouriteGenre == "puzzle":
    # Display Games
    print("""
Available Games:
Block Drop - $10
Maze Runner - $5
    """)

else:
    print(f"There are no games for the {favouriteGenre} genre.")

