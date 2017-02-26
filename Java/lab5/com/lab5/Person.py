"""Person class"""
from Date import *
#super class
class Person(object):
    firstName = ""
    surname = ""
    date = Date(0, 0, 0)
    gender = ""


    def __init__(self,firstName, surname, date,gender):

        self.firstName = firstName
        self.surname = surname
        self.date = date
        self.gender = gender

        #print("person created")

    def __str__(self):
        return "\n\nName: {} {} \nDOB:{} \nGender:{}".format(self.firstName,self.surname,self.date,self.gender)
