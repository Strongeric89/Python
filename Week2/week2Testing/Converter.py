def getNumber():
    number = -1
    isRunning = True
    while isRunning:
        number = int(raw_input("please enter your number:"))
        # check if number is greater than 0
        if(number != 0):
            print("thank you. you entered " + str(number))
            return number
        else:
            print("not a valid number. try again!")

#dec to bin conversion algorithm
def binNumber(number):
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary

#dec to bin conversion algorithm
def decNumber(number):
    decimalNum = int(number,2)
    return decimalNum

def customNumber(number):
    base = int(raw_input("Enter your base: "))
    binary = ''
    while number > 0:
        binary = str(number % base) + binary
        number = number // base
    return binary






#the following program is a converter
number = ''
option = int(raw_input("[1]Decimal to Binary\n[2]Binary to Decimal\n[3]Your own\n"))

if option == 1:
    print("you chose Binary to Decimal.")
    number = getNumber()
    print("converting....")
    binary =binNumber(number)
    print(binary)


elif option == 2:
    print("you chose Decimal to binary.")
    number = getNumber()
    newNum = str(number)
    print("converting....")
    decimal = decNumber(newNum)
    print(decimal)

elif option == 3:
    print("you chose your own conversion.")
    number = getNumber()

    newNumber = customNumber(number)
    print("Converting....")
    print("your custom number is " + str(newNumber))

else:
    print("not a valid option")