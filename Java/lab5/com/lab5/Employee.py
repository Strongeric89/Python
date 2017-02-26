"""Employee class- inherits from Person"""
from Person import *
from Job import *
from Date import *
from FileIO import *
class Employee(Person):
    job = Job(0.00,"a role",0)
    personnelNumber = int(0)
    startDate = Date(0,0,0)

    def __init__(self,firstName,surname,date,gender,job,personnelNumber,startDate):
        #calling the super constructor
        super(Employee,self).__init__(firstName,surname,date,gender)
        self.job = job
        self.personnelNumber = personnelNumber
        self.startDate = startDate


    def __str__(self):
        s = super(Employee,self).__str__()
        str1 = ""
        str1 += s + "\nJob: {} \nPersonnel Number: {} \nStart Date: {} ".format(self.job,self.personnelNumber, self.startDate)

        ##PART 4##
        file = FileIO("names.txt")
        file.writeFile("names.txt",str1)
        return str1