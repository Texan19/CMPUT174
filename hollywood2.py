filename = input("Please enter the file name: ")

# - Variables - #
file = open(filename, "r")
actors = []
movies = []
correctMovie = ""
content = file.readlines()
file.close()

# - Welcome Message - #
welcomeMessage = "Welcome to Hollywood Night!"
print("=" * len(welcomeMessage))
print(welcomeMessage)
print("=" * len(welcomeMessage))

# - Processing - #
for lines in content:
    line = lines.strip().split(",")
    actors.append(line[0]) # appends the data before the ","
    movies.append(line[1]) # appends the data after the ","

for i in range(len(actors)):
    for j in range(len(movies)):
        if i == j: # check if the indexes match
            print(f"{i+1}. {actors[i]}") # use i+1 since the index always starts at zero

while True:
    attempts = 1
    if filename in ("stars1.txt", "stars2.txt"):
        actorChoice = int(input(f"Please enter a number between 1 and {len(actors)}: "))
        for i in range(len(actors)):
            if actorChoice == i+1: # use i+1 since the index always starts at zero
                print(f"The chose actor is {actors[i]}")
                correctMovie = str(movies[i])

    while attempts <= 3:
        print(f"ATTEMPT {attempts}")
        movieGuess = input("Guess the movie: ")
        if movieGuess == correctMovie:
            print("Correct! Well done, Player")
            break
        elif attempts != 3:
            print("Incorrect. Please try again")
            attempts += 1
        elif attempts == 3:
            print(f"Out of guesses. Correct answer was {correctMovie}")
            attempts += 1

    goAgain = input("Would you like to play again? (y/n): ").lower()

    if goAgain == "y":
        pass
    else:
        break

