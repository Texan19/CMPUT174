filename = input("Please enter the file name: ")

# - Variables - #
file = open(filename, "r")
actors = []
movies = []
content = file.readlines()
file.close()

# - Welcome Message - #
welcomeMessage = "Welcome to Hollywood Night!"
print("==" + ("=" * len(welcomeMessage)) + "==")
print("  " + welcomeMessage + "  ")
print("==" + "=" * len(welcomeMessage) + "==")

# - Processing - #
for lines in content:
    line = lines.strip().split(",")
    actors.append(line[0]) # appends the data before the ","
    movies.append(line[1]) # appends the data after the ","

for i in range(len(actors)):
    for j in range(len(movies)):
        if i == j: # check if the indexes match
            print(f"{i+1}. {actors[i]} - {movies[j]}") # use i+1 since the index always starts at zero

if filename in ("stars1.txt", "stars2.txt"):
    actorChoice = int(input(f"Please enter a number between 1 and {len(actors)}: "))
    for i in range(len(actors)):
        if actorChoice == i+1: # use i+1 since the index always starts at zero
            print(f"The chose actor is {actors[i]}")