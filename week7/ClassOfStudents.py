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
#create a class of students
classDT211c = []
isRunning = True
while(isRunning):
    first = raw_input("Please enter your first name: ")

    if(first =="end" or first =="END"):
        break

    last = raw_input("please enter your surname: ")

    id = raw_input("please enter your Student ID: ")
    print("-"*30)
    #create the instance
    first = Student(first,last,id)
    classDT211c.append(first)
print("Class List DT211c")
for student in classDT211c:
    print(student)

#implementing setters and getters
testCase = raw_input("enter a student name in the list:")
#print(classDT211c[first])



