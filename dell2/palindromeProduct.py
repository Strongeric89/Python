#get the input save as a string to include 0 value.
number = raw_input("Enter a number:" )

# get the reverse of the 3 digit number
revNum = number[::-1]

#concat the numbers to create the palidrome
palindrome = number + revNum

#convert to int data type
newNumber = int(palindrome)

#check if it is a palidrome
if(newNumber == int(palindrome)):
    print(newNumber)
    isRunning = True
    num1 = 0
    num2 = 0
    i= 0
    j=0
    while(isRunning):
        if (i * j == newNumber):
            if (i > 100 and j > 100 and j < 1000):
                num1 = i
                num2 = j
                break
        j += 1
        if (j == newNumber):
            j = 0
            i += 1

    print("{} * {} = {}".format(num1,num2,newNumber))

else:
    print("not a palindrome")
