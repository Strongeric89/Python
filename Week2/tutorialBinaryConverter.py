"""The following program is for the tutorial class on week 2
a decimal to binary converter and binary to decimal converter
"""

#part 1
decimalNumber=int(raw_input("Please enter your number : "))
number = decimalNumber
print("you entered " + str(decimalNumber) )
binString = ""

while(decimalNumber > 0):
    #divide the number by two and take its remainder
    binString = str(decimalNumber % 2) + binString
    decimalNumber = decimalNumber // 2
print("The Binary Number of " + str(number) +  " is " +  binString)

#part 2convert a binary sequency back to a decimal
binNumber = int(binString,2)
print("\n\nThe binary Number " + str(binString))
print("The Decimal version of is " + str(binNumber))


#HEX CONVERSION
#array of numbers to show the index of the new number
numbers = [1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
#algorithm to get the hex version

string = ''

while number > 0:
    r = int(number % 16)
    number = number // 16
    if r > 9:
        string = str(numbers[r-1])+ string
    else:
        string = str(r) + string

print("\n\nHex version: 0x"+ string)




