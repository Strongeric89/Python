#the following program is the fiboannaci sequence

def fibonacci(sequence):
    list = []
    num1 = 0
    num2 = 1
    num3 = num1 + num2
    i = 0
    list.append(num1)
    list.append(num2)
    list.append(num3)

    isRunning = True
    while (isRunning):
        if (i == sequence):
            isRunning = False
        else:
            num1 = num2
            num2 = num3
            num3 = num1 + num2

            i = i + 1
            list.append(num3)

    return list

def perfectInput():
    isRunning = True

    while(isRunning):
        try:
            sequence = int(raw_input("Please enter the sequence of numbers: "))
        except ValueError:
            print("not a valid number. Try again!")
            isRunning = True
        else:
            sequence = sequence - 3
            isRunning = False


    return sequence


listOfNumbers = []
sequence = perfectInput()
listOfNumbers = fibonacci(sequence)
sequence = sequence + 3
print("the fibonacci sequence of " + str(sequence) + " numbers is:  ")
print(listOfNumbers)

