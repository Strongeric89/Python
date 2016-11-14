"""
The following program is lab 9, Vector class
adding, subtracting , multiply etc..

"""

#create the class
class Vector(object):
    x=0
    y=0
    id=0

    #instance of the vector
    def __init__(self, id, x=0,y=0):
        self.x=x
        self.y=y
        self.id=id



    #str representation of the vector
    def __str__(self):
        return "vector {}: ({},{})".format(self.id,self.x,self.y)

    def __add__(self,v2):

        x1 = self.x + v2.x
        y1 = self.y + v2.y

        #constructing new vector
        v3 = Vector(3,x1,y1)
        return v3

    def __sub__(self,v2):
        x1 = self.x - v2.x

        y1 = self.y - v2.y
        # constructing new vector
        v3 = Vector(3, x1, y1)
        return v3


    def __mul__(self, v2):
        #this needs to be fixed
        x1 = self.x * v2.x + self.x * v2.y
        y1 = self.y * v2.y + self.y * v2.x

        # constructing new vector
        v3 = Vector(3, x1, y1)
        return v3


    def __mag__(self,v1):
        x1 = self.x * v1.x
        y1 = self.y * v1.y
        # constructing new vector
        v3 = Vector(3, x1, y1)
        return v3


def getVector():
    id = int(raw_input("Please enter ID for Vector: "))
    x = int(raw_input("Please enter value for X: "))
    y = int(raw_input("Please enter value for Y: "))

    vector = Vector(id,x,y)
    vectorList.append(vector)

    return vector

#main
vectorList = []
while(True):
    option=int(raw_input("[1]Add two vectors\n[2]Subtract two Vectors\n[3]Multiply Two Vectors\n[4]Magnitude\n[5]Quit\n[6]Print all Vectors\nUSER:"))

    if (option == 1):
        print("You selected Add two Vectors")
        # create two vector
        v1 = getVector()

        v2 = getVector()

        #v3 = v1.__add__(v2)
        v3 = v1 + v2
        vectorList.append(v3)
        print(v3)

    elif(option ==2):
        print("You selected Subtract two Vectors")
        # getting co-ordinates
        v1 = getVector()

        v2 = getVector()

        #v3 = v1.__sub__(v2)
        v3 = v1 - v2
        vectorList.append(v3)
        print(v3)

    elif(option ==3):
        print("You selected Multiply two Vectors")
        # create two vector objects
        v1 = getVector()

        v2 = getVector()

        #v3 = v1.__mult__(v2)
        v3= v1 * v2
        vectorList.append(v3)
        print(v3)

    elif(option ==5):
        print("Exit")
        break

    elif (option == 4):
        print("You selected Magnitude of a Vector")
        # create two vector objects
        v1 = getVector()

        v3 = v1.__mag__(v1)
        #v3 = v1 ** v1
        vectorList.append(v3)
        print(v3)

    elif (option == 6):
        #print all items in the list
        print("print all vectors.........")
        for vector in vectorList:
            print("Vector ID:{} X:{} Y:{}\t type:{}".format(vector.id,vector.x,vector.y,type(vector)))


    else:
        print("Not a valid option. Try Again")