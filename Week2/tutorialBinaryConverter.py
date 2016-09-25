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

base = raw_input("Please enter a base to convert to: ")
newNumber = int(binString,int(base))
print(newNumber)



