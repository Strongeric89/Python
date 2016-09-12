"""The following program checks for numbers"""

import math

num1 = int(raw_input("Enter the first number"))
num2 = int(raw_input("Enter the second number"))
num3 = int(raw_input("Enter the third number"))

#return the largest and smallest numbers
minNum = min(num1,num2,num3)
maxNum = max(num1,num2,num3)

print("The min Number is " + str(minNum)+ "\nThe max Number is" + str(maxNum) )

if(num1 != minNum | num1 !=maxNum):
    print(str(num1) +" is the middle number")

if (num2 != minNum | num2 != maxNum):
    print(str(num2) + " is the middle number")

if (num3 != minNum | num3 != maxNum):
    print(str(num3) + " is the middle number")

