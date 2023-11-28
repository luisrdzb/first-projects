print("Welcome to my general knowledge quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Ok! Let's play!")
score = 0

answer = input("How many days does it take for the Earth to orbit the Sun? ")
if answer == "365":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("When was Netflix founded: 1997, 2001, 2009, 2015? ")
if answer == "1997":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many stripes are there on the US flag? ")
if answer == "13":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many ghosts chase Pac-Man at the start of each game? ")
if answer == "4":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many dots appear on a pair of dice? ")
if answer == "42":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")