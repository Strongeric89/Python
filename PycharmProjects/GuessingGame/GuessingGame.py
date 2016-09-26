import random
#the following program is for a guessing game

print("Welcome to the guessing Game.")
print("generating random number...")
lives = 10
#generate random number between 1-99
gameNumber= random.randint(1,100)
flag = 0
isRunning = True
#print(gameNumber)
while(isRunning):
    if(lives == 1):
        isRunning = False
        flag = 1

    guess = int(raw_input("lives=" + str(lives) + "\nGuess number:"))
    if(guess == gameNumber ):
        flag = 0
        isRunning = False
    else:
        print("try again!")
        lives = lives - 1

if flag == 1:
    print("You ran out of Lives! you lost...")
    print("the number was " +  str(gameNumber))
else:
    print("Congrats you won!")




