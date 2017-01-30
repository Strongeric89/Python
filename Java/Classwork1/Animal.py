"""The following program is to mirror the classwork1 in java - so that python synthax is still in my head for exam"""

#part 1 create animal class
class Animal(object):
    #attributes
    __name__=""
    __age__= 0
    __type__=""
    __sex__="undefined"

        #first constructor
    def __init__(self,name="null",age=0,type="null"):
        self.__name__ = name
        self.__age__ = int(age)
        self.__type__ = type

        #second constructor
    def __init__(self,name="null",age=0,type="null",sex="undefined"):
        self.__name__ = name
        self.__age__ = int(age)
        self.__type__ = type
        self.__sex__ = sex

        #tostring method
    def __str__(self):
        return "name:" + self.__name__ + "\nage:" + str(self.__age__) + "\ntype:" + self.__type__ + "\nSex:" + self.__sex__

    def run(self):
        print(self.__name__ + " is running......")

    def eat(self):
        print(self.__name__ + " is eating.....")

    def sleep(self):
        print(self.__name__ + " is sleeping.....")




#main
#a list of animals
animals = []

#create objects of animal
dory = Animal("dory",3,"bluefish","F")
nemo = Animal("nemo",1,"clownfish","M")

animals.append(dory)
animals.append(nemo)


#print results in for loop
for animal in animals:
    print(animal)

dory.eat()
nemo.sleep()