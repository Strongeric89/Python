"""
The following program is lab 9, Vector class
adding, subtracting , multiply etc..

"""

#create the class
class Vector(object):
    #variables
    tup1=(0,0)
    tup2=(0,0)


    #instance of the vector
    def __init__(self, tup1,tup2):
        self.tup1=tup1
        self.tup2=tup2

    #str representation of the vector
    def __str__(self):
        return "vector: {} {}".format(self.tup1,self.tup2)

    def __add__(self,tup1,tup2):
        x,y = tup1
        a,b = tup2
        x1 = x + a
        y1 = y + b
        addedTup = (x1,y1)
        print("in addition")
        return "vector: {}".format(addedTup)

    def __sub__(self,tup1,tup2):
        x,y = tup1
        a,b = tup2
        x1 = x - a
        y1 = y - b
        subTup = (x1,y1)
        print("in subtract")
        return "vector: {}".format(subTup)

    def __mult__(self,tup1,tup2):
        x,y = tup1
        a,b = tup2
        x1 = x * a
        y1 = y * b
        multTup = (x1,y1)
        print("in subtract")
        return "vector: {}".format(multTup)


def getVector(id):
    print("Vector %d" % id)
    x= int(raw_input("Please enter value for X: "))
    y = int(raw_input("Please enter value for Y: "))
    vector= (x,y)
    return vector

#main


mainVector = (0,0)
while(True):
    option=int(raw_input("[1]Add two vectors\n[2]Subtract two Vectors\n[3]Multiply Two Vectors\n[5]Quit\nUSER:"))

    if (option == 1):
        print("You selected Add two Vectors")
        # create two vector objects
        tup1 = getVector(1)
        tup2 = getVector(2)

        addedTup = Vector(tup1,tup2)
        print(addedTup.__add__(tup1,tup2))


    elif(option ==2):
        print("You selected Subtract two Vectors")
        # create two vector objects
        tup1 = getVector(1)
        tup2 = getVector(2)

        subTup = Vector(tup1, tup2)
        print(subTup.__sub__(tup1, tup2))


    elif(option ==3):
        print("You selected Multiply two Vectors")
        # create two vector objects
        tup1 = getVector(1)
        tup2 = getVector(2)

        multTup = Vector(tup1, tup2)
        print(multTup.__mult__(tup1, tup2))
    elif(option ==4):
        print("Exit")
        break

    else:
        print("Not a valid option. Try Again")