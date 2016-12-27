"""
the following program is for Lab Test 2, Semester 1, Python
Author: Eric Strong C15708709
Date: 24/11/2016
Description: Classes with complex numbers
Version: Python 2.7.11
Platform: Windows 10, PyCharm Community Edition 2016.2.3
NOTE: using raw_input instead of input as my version of python only supports that
"""

class ComplexNumber(object):

    def __init__(self,a,b,i,symbol):
        self.a = a
        self.b = b
        self.i = i
        self.symbol = symbol

    def __str__(self):
        return "{}{}{}{}\n".format(self.a,self.symbol,self.b,self.i)

    def __add__(self,complexNum2):

        x1 = self.a + complexNum2.a
        y1 = self.b + complexNum2.b
        symbol = self.symbol
        num = ComplexNumber(x1, y1, "i", symbol)
        return num


    def __sub__(self,complexNum2):
        x1 = self.a - complexNum2.a
        y1 = self.b - complexNum2.b
        symbol = " "
        num = ComplexNumber(x1, y1, "i", symbol)
        return num

    def __mul__(self,num):
        x1 = (self.a * complexNum2.a) - (self.b * complexNum2.b)
        y1 = (self.a * complexNum2.b) + (self.b * complexNum2.a)

        symbol = "+"
        num = ComplexNumber(x1, y1, "i", symbol)
        return num

    def __addInt__(self,num):
        x1 = (num + self.a)
        y1 = (self.b)
        symbol = "+"
        newNum = ComplexNumber(x1,y1,"i",symbol)
        return newNum

    def __multInt__(self,num):
        x1 = (num * self.a)
        y1 = (num * self.b)
        symbol = "+"
        newNum = ComplexNumber(x1,y1,"i",symbol)
        return newNum

def getNumbers(symbol,i):

    print("Complex Number:" + str(i))
    while(True):
        try:
            a = int(raw_input("Enter (a): "))
            break
        except ValueError:
            print("not a valid type. Int only")

    while(True):
        try:
            b = int(raw_input("Enter (b): "))
            break
        except ValueError:
            print("not a valid type. Int only")

    #create an instance of the complex Number clasee
    num = ComplexNumber(a,b,"i",symbol)
    return num

#main
print("Complex Number Calculator.....\n")
complexNum1 = getNumbers("+",1) # + is only for representation purposes
complexNum2 = getNumbers("+",2)  # + is only for representation purposes

while(True):

    while(True):
        try:
            option = int(raw_input("[1]Addition\n[2]Subtraction\n[3]Multiplication\n[4]Complex and an Integer\n[5]Quit\n[6]Complex X Int\nUSER:"))
            break
        except ValueError:
            print("numbers [1-6] only")
    if(option == 1):
        #add two complex numbers

        print("num 1: " + str(complexNum1))
        print("num 2: " + str(complexNum2))
        if(type(complexNum1) == ComplexNumber and type(complexNum2) == ComplexNumber):
            sum = complexNum1 + complexNum2
            print("The sum of both is: " + str(sum))
        else:
            print("not valid numbers:")

    elif(option == 2):
        #subtract two complex numbers

        print("num 1: " + str(complexNum1))
        print("num 2: " + str(complexNum2))

        if (type(complexNum1) == ComplexNumber and type(complexNum2) == ComplexNumber):
            sum = complexNum1 - complexNum2
            print("The sum of both is: " + str(sum))
        else:
            print("Not valid type")

    elif (option == 3):
        #multiply two complex numbers

        print("num 1: " + str(complexNum1))
        print("num 2: " + str(complexNum2))
        if (type(complexNum1) == ComplexNumber and type(complexNum2) == ComplexNumber):
            sum = complexNum1 * complexNum2
            print("The sum of both is: " + str(sum))

    elif (option == 4):
        #int and complex
        num = int(raw_input("enter an integer number: "))
        #complexNum1 = getNumbers("+",1)
        if (type(complexNum1) == ComplexNumber and type(num) == int):
            sum = complexNum1.__addInt__(num)
            print("The sum of both is: " + str(sum))
        print("not valid type")

        num = int(raw_input("enter an integer number: "))
        if (type(complexNum1) == ComplexNumber and type(num) == int):
            sum = complexNum2.__addInt__(num)
            print("The sum of both is: " + str(sum))
        else:
            print("not Valid type")


    elif (option == 5):
        print("Game over")
        break

    elif (option == 6):
        # int and complex
        num = int(raw_input("enter an integer number: "))
        # complexNum1 = getNumbers("+",1)
        if (type(complexNum1) == ComplexNumber and type(num) == int):
            sum = complexNum1.__multInt__(num)
            print("The sum of both is: " + str(sum))
        print("not valid type")

        num = int(raw_input("enter an integer number: "))
        if (type(complexNum1) == ComplexNumber and type(num) == int):
            sum = complexNum2.__multInt__(num)
            print("The sum of both is: " + str(sum))
        else:
            print("not Valid type")
    else:
        print("Not a valid Option")
print("End of program...")
