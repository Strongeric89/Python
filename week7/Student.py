class Student(object):
    firstName=''
    lastName=''
    idNum=''
    def __init__(self,first='',last='',id=''):
        self.firstName = first
        self.lastName = last
        self.idNum = id

    def __str__(self):
       return "{} {} {}".format(self.firstName, self.lastName, self.idNum)

    #setter
    def setName(self, first,last):
        self.firstName = first
        self.lastName = last
    #getter
    def getName(self):
        return "{} {} ".format(self.firstName,self.lastName)

    def run(self):
        return "{} is Running".format(self.firstName)


#creating an instance of the student class
eric = Student("eric","Strong","C15")

laura = Student("laura","Bermingham","B13")

Student.idNum = "ccccc"
ger = Student("Ger","Strong")



# print(eric)
# print(eric.run())
# print(eric.idNum)
# 
# print(laura)
# print(laura.run())
#
# print(ger)
#
# eric.setName("Eric","Strong")
#
# #print(eric)
# eric.getName()
