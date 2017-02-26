from Date import *
from Job import *
from Person import *
from Employee import *
from FileIO import *

#part 1
now= Date(26,02,2017)
job1 = Job(45.500,"Software Developer",7)

print(now)
print(job1)

#part 2
# type: (firstName, surname, date, gender) -> Person
# p1 = Person("Eric","Strong",Date(02,03,1989),"Male")
# print(p1)
# emp2 = Employee("Laura","Bermingham", Date(19,11,1990),"Female","Software Tester",636,Date(26,02,2017))
# print(emp2)

#part 3
newFile = FileIO("roles.txt")
# print(newFile)
# print(newFile.readFile())

#lets set the job title to this new content
emp3 = Employee("Eric","Strong", Date(02,03,1989),"Male",Job(56.000,"blank",2),10,Date(26,02,2017))
print(emp3)

emp4 = Employee("Laura","Strong", Date(19,9,1990),"Female",Job(45.0000, "blank",6),12,Date(26,02,2017))
print(emp4)


emp5 = Employee("Dave","Bermo", Date(20,11,1967),"male",Job(34.0000, "blank",3),11,Date(26,02,2017))
print(emp5)


emp6 = Employee("Ger","Strong", Date(3,2,1987),"male",Job(33.0000, "blank",12),13,Date(26,02,2017))
print(emp6)





