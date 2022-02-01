heading="Number guessing game"
chances=1
number=6
print(heading)

SubHeading="Guess a number between 1 and 9"
print(SubHeading)
while chances < 5:
    guess=input("Enter Number")
    chances=chances+1
    print(chances)
    if guess == number:
        print("Congratulations you won")
        #if not chances < 5:
        #print("You Lost")
