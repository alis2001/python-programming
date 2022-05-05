import random
userWins = 0
computerWins = 0

options = ["rock", "paper", "scissors"]
while True:
    userInput = input("Type Rock/Paper/Scissors or Q to quit the game!",).lower()
    if userInput == "q":
        break
    if userInput not in options:
        continue
    randomNumber = random.randint(0, 2) #rock -> 0 paper -> 1 scissors -> 2
    computerOption = options[randomNumber]
    print("Computer picked", computerOption + ".")
    if userInput == "rock" and computerOption == "scissors":
        print("You Won!")
        userWins += 1


    elif userInput == "paper" and computerOption == "rock":
        print("You Won!")
        userWins += 1


    elif userInput == "scissors" and computerOption == "paper":
        print("You Won!")
        userWins += 1

    elif userInput == computerOption:
        print("Draw")



    else:
        print("You Lost!")
        computerWins += 1

print("You Won", userWins, "times.")
print("The computer won", computerWins, "times.")
print("Goodbye")


