#superclass
class Person(object):
    health = 100
    arms=0
    legs=0
    name=""

    def __init__(self,arms=2,legs=2,name=""):
        self.arms = arms
        self.legs = legs
        self.name = name

    def __str__(self):
        return "my name is {}. I have {} arms and i have {} legs".format(self.name,self.arms,self.legs)

    def setHealth(self,health):
        self.health = health

    def run(self):
        print("%s is runnning" % self.name)
        self.health = self.health - 50

    def sleep(self):
        self.health = 100


class Student(Person):
    ID=""

    def __init__(self,id,name):
        self.ID= id
        self.name = name

    def __str__(self):
        return "{} is a student. Id: {}".format(self.name,self.ID)



#main

cian = Person(2,2,"cian")
print(cian)
cian.run()
print(cian.health)
cian.sleep()
print(cian.health)
print(type(cian))