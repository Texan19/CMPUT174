filename = input("Please enter the file name: ")

# - Variables - #
file = open(filename, "r")
actors = []
movies = []
correctMovie = ""
totalPoints = 0
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
    # - VARIABLES THAT RESET EACH ROUND - #
    attempts = 1
    roundPoints = 3
    roundHintUsed = False

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
            if roundHintUsed:
                roundPoints /= 2
                totalPoints += roundPoints
                print(f"Points Earned: {roundPoints}")
            else:
                totalPoints += roundPoints
                print(f"Points Earned: {roundPoints}")
            break

        if attempts == 1:
            print("Incorrect. Please try again")
            roundPoints -= 1
            hint1 = input("Would you like a hint? (y/n): ").lower()
            if hint1 == "y":
                roundHintUsed = True
                words = correctMovie.split()
                print(f"Hint 1: The movie title has {len(words)} word(s)")
                attempts += 1
            else:
                attempts += 1

        elif attempts == 2:
            print("Incorrect. Please try again")
            roundPoints -= 1
            hint2 = input("Would you like a hint? (y/n): ").lower()
            if hint2 == "y":
                roundHintUsed = True
                words = correctMovie.split() # split the words of the movie name
                maskedWords = []
                for word in words:
                    maskedWords.append(word[0] + '*' * (len(word)-1) + " ")
                hintText = "".join(maskedWords)
                print(f"Hint 2: The movie title is {hintText}")
                attempts += 1
            else:
                attempts += 1

        elif attempts == 3:
            print(f"Out of guesses. Correct answer was {correctMovie}")
            roundPoints -= 1
            print(f"Points Earned: {roundPoints}")
            attempts += 1

    goAgain = input("Would you like to play again? (y/n): ").lower()

    if goAgain == "y":
        pass
    else:
        print(f"Total Points: {totalPoints}")
        if 0 <= totalPoints < 6:
            print("No ticket. Better luck next screening. You suck. Ha Ha Ha!")
        elif 6 <= totalPoints < 11:
            print("Matinee material. Keep watching!")
        elif 11 <= totalPoints < 16:
            print("Certified fresh. Nice Work!")
        elif totalPoints >= 16:
            print("Oscar-worthy! You belong in Hollywood!")

        print("Thank you for playing. Goodbye!")
        break
