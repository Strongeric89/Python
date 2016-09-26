import math
#the following program will calculate the area of a circle
radius = float(raw_input("what is the Radius?"))
pi = math.pi
rSq = radius **2
areaOfCircle = pi * rSq
print("The Area of the Circle is {:.2f} CMsq".format(areaOfCircle))
