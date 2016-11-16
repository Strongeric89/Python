#super class
class Shape(object):
    width=0
    height=0
    name=""

    def __init__(self,name,x=0,y=0):
       self.name = name
       self.width = x
       self.height = y

    def area(self):
        return self.width * self.height

    def __str__(self):

        return "{} Width:{} Height:{} area:{}".format(self.name,self.width,self.height,self.area())

class Triangle(Shape):
    def __init__(self,name,x,y):
        self.width=x
        self.height=y
        self.name= name

    def area(self):
        areaTriangle = float(float(self.width / 2) * float(self.height))
        return areaTriangle

class Square(Shape):
    def __init__(self, name, x, y):
        self.width = x
        self.height = y
        self.name = name

    def area(self):
        areaSquare = float(float(self.width) * float(self.height))
        return areaSquare

class Circle(Shape):
    radius = 0
    pi = 3.14
    def __init__(self, name, x, r):
        self.width = x
        self.radius = r
        self.name = name

    def area(self):
        areaCircle = self.pi * (self.radius*self.radius)
        return areaCircle
#main
shapes = []
#create a shape
square = Square("Square",3.0,3.0)
shapes.append(square)
triangle = Triangle("Triangle",3.0,3.0)
shapes.append(triangle)
circle = Circle("Circle",10,5)
shapes.append(circle)

#print out shapes
for shape in shapes:
    print(shape)





