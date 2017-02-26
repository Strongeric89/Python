"""Job class"""
from FileIO import *
class Job(object):
    salary = float(0.00)
    role= ""
    jobID = int(0)
    #added for part 3
    possibleJobs = []

    def __init__(self, salary,role,jobID):
        self.salary= salary
        #self.role = role
        self.jobID = jobID

        ##part 3
        self.selectJobRole()
        self.role = self.possibleJobs[self.jobID] ##this should be whatever id the user specifies in the constructor

    def __str__(self):
        return "Salary: {}\nRole:{}\nJobId:{}".format(self.salary,self.role,self.jobID)


    def selectJobRole(self):
        file = FileIO("roles.txt")
        self.possibleJobs = file.readFile()
