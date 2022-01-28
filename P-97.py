heading="Number guessing game"
print(heading)
EnterNumber="Guess a number between 1 and 9"
while chances < 5:
    if guess == number:
        print("Congratulations you won")
        if not chances < 5:
        print("You Lost")
