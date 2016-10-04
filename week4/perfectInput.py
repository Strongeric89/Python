print("the following program simulates a perfect input")
isRunning = True
while(isRunning):
    try:
        number = int(raw_input("enter a number: "))

    except ValueError:
        print("not a valid number type try again!:")
        isRunning = True
    else:
        print("you entered " +  str(number))
        isRunning = False

print("EXIT: outside loop")