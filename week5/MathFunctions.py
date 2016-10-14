"""We will represent a fraction as a 2 element tuple. The first element of thetuple is the numerator, and the second element is the denominator. """

#gcd
def getGCD(numbers):
    a = numbers[0]
    b = numbers[1]
    print("getting GCD of " + str(numbers))
    if (a < b):
        n = a
        a = b
        b = n

    while (b != 0):
        r = b
        b = a % r
        a = r
    return a

def getFraction():

    #step 1 get the user input
    numerator = int(raw_input("Please enter your Numberator: "))
    denom = int(raw_input("please enter your Denominator: "))
    fraction = (numerator,denom)
    return fraction

def getNumbers():
    num1 = int(raw_input("please enter your first Number:"))
    num2 = int(raw_input("please enter your second Number: "))
    numbers = (num1,num2)
    return numbers


#LCM
def lcm():

    list1 = []
    list2 = []
    num1 = int(raw_input("please enter your first Number:"))
    num2 = int(raw_input("please enter your second Number: "))

    isRunning = True
    lcm = 0
    test1=int(num1)
    test2=int(num2)
    while(isRunning):
        if(test1 == 100 or test2 == 100):
            lcm=test1
            break

        test1 += num1
        list1.append(test1)
        test2 +=num2
        list2.append(test2)

    i=0
    j=0
    while(True):
        if(list1[i] == list2[j]):
            lcm = list1[i]
            break
        i +=1
        if(i == len(list1)):
            i = 0
            j +=1

    return lcm

#addFraction

def addFraction():
    firstFraction = getFraction()
    secondFraction = getFraction()

    #algorithm to add two fractions
    #find the lcm
    lcm = firstFraction[1] * secondFraction[1]
    numer1 = lcm / firstFraction[1]
    numerator1New = numer1 * firstFraction[0]

    firstFrac1 = (numerator1New, lcm)

    numer2 = lcm / secondFraction[1]
    numerator2New = numer2 * secondFraction[0]

    secondFrac1 = (numerator2New,lcm)

    fraction = (numerator1New + numerator2New, lcm)

    print(str(firstFrac1) + "+" + str(secondFrac1) + "=" + str(fraction))
    return fraction



#subtractFraction
def subFraction():
    firstFraction = getFraction()
    secondFraction = getFraction()

    #algorithm to add two fractions
    #find the lcm
    lcm = firstFraction[1] * secondFraction[1]
    numer1 = lcm / firstFraction[1]
    numerator1New = numer1 * firstFraction[0]

    firstFrac1 = (numerator1New, lcm)

    numer2 = lcm / secondFraction[1]
    numerator2New = numer2 * secondFraction[0]

    secondFrac1 = (numerator2New,lcm)

    fraction = (numerator1New - numerator2New, lcm)

    print(str(firstFrac1) + "+" + str(secondFrac1) + "=" + str(fraction))
    return fraction


#reduceFraction
def reduce():
    firstFraction = getFraction()

    # algorithm to reduce a fractions

    i=2
    gcd = 2
    while(True):
        if(i % firstFraction[0] == 0 and i % firstFraction[1] == 0):
            gcd = i
            break
        i+=1

    #to reduce down the fraction
    top = gcd / firstFraction[0]
    bottom = gcd / firstFraction[1]

    newFraction = (top,bottom)

    print(newFraction)
    return newFraction



#main

while(True):
    ent = raw_input("press enter to continue: ")


    option = int(raw_input("Pick an option:\n[1]GCD\n[2]LCM\n[3]Add Fraction\n[4]Subtract Fraction\n[5]Reduce Fraction\n[0]QUIT:\nUSER: "))


    if (option == 1):
        print("GCD")
        numbers = getNumbers()


        answer = getGCD(numbers)
        print("the GCD is : " + str(answer))

    elif(option == 2):
        print("LCM")
        answer =lcm()
        print("The LCM is : " + str(answer))


    elif(option ==3):
        print("add fractions")
        answer = addFraction()
        print("your new Fraction is " + str(answer))



    elif(option ==4):
        print("subtract fractions")
        answer = subFraction()
        print("your new Fraction is " + str(answer))

    elif(option == 5):
        print("Reduce Fraction")
        answer = reduce()
        print("your reduced fraction is " + str(answer))

    elif(option == 0):
        print("Game over!")
        break


    else:
        print("not a valid Option!")
