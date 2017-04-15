#The following program is lab 1 - revisited on 14/4/17 for prep for exams

"""You prompt for an integer, convert the integer to a binary number string (there is no
type for actual binary numbers so we just represent it as a string). We then take the
string and turn it back into a regular integer"""
def algorithm():
    # prompt user to enter a number
    decimalNumber = int(raw_input("Please enter a decimal number to be converted to binary:  "))

    if (decimalNumber == 0):
        print("not a valid Number: It is " + str(decimalNumber))
    elif (decimalNumber < 0):
        print("not a valid Number: It is Negative " + str(decimalNumber))
    else:

        num = decimalNumber
        binString = ''
        while (decimalNumber > 0):
            binString = str(decimalNumber % 2) + binString
            decimalNumber = decimalNumber // 2
        print("The Binary Number of " + str(num) + " is " + binString)

        #convert back to decimal
        length = len(binString)
        num = 0
        for i in range(length):
            num = num + int(binString[i])
            num = num * 2
        print num/ 2





def easyWay():
    #simple string formats of the number before the algorithm
    # prompt user to enter a number
    decimalNumber = int(raw_input("Please enter a decimal number to be converted to binary:  "))

    binaryStr = "Decimal: {0:d}\nBinary: {0:b}\nHex: {0:X}\nOctal: {0:o}".format(decimalNumber)
    print(binaryStr)


def chooseBase():
    #simple string formats of the number before the algorithm
    # prompt user to enter a number
    decimalNumber = int(raw_input("Please enter a decimal number to be converted:  "))
    base = int(raw_input("please choose your base: "))

    if (decimalNumber == 0):
        print("not a valid Number: It is " + str(decimalNumber))
    elif (decimalNumber < 0):
        print("not a valid Number: It is Negative " + str(decimalNumber))
    else:

        num = decimalNumber
        binString = ''
        while (decimalNumber > 0):
            binString = str(decimalNumber % base) + binString
            decimalNumber = decimalNumber // base
        print("The custom based Number of " + str(num) + " is " + binString)

        # convert back to decimal
        length = len(binString)
        num = 0
        for i in range(length):
            num = num + int(binString[i])
            num = num * base
        print num / base


#make shift-switchcase
call = int(raw_input("[1] algorithm\n[2] easyway\n[3]Choose Base"))

options = {1:algorithm, 2:easyWay,3:chooseBase}
print (options[call]())