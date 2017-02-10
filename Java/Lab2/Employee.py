#CLASS DECLARATIONS

#EMPLOYEE CLASS
class Employee(object):
    #attributes
    __firstName__=""
    __surName__=""
    __staffNumber__=int(0)
    __baseAnnualSalary__=float(0.00)
    __startDate__=""

    #super constructor
    def __init__(self, firstName,surName,staffNumber, baseAnnualSalary, startDate):
        self.__firstName__ = firstName
        self.__surName__ = surName
        self.__staffNumber__=int(staffNumber)
        self.__baseAnnualSalary__=float(baseAnnualSalary)
        self.__startDate__=startDate

        print(self.__firstName__ + " was added to the System")

    def calculatePay(self):
        #baseAnnual / 12
        pay = float(self.__baseAnnualSalary__ / 12)
        return pay

    #str method
    def __str__(self):
        info =  "\nname:" + self.__firstName__ + " " + self.__surName__ + "\nEmployee Number: " + str(self.__staffNumber__) + "\nStart Date: " + self.__startDate__
        if(self.__baseAnnualSalary__ > 0.00):
            return info + "\nsalary: " + str(self.__baseAnnualSalary__)

        else:
            return info

    #getters and setters - come back to later

#HOURLY EMPLOYEE CLASS
class HourlyEmployee(Employee):
    #attributes
    __hoursWorked__=0
    __hourlyRate__=0

    #super(Num2,self).__init__(num)

    def __init__(self,firstName,surName,staffNumber, baseAnnualSalary, startDate, hoursWorked, hourlyRate):
       super(HourlyEmployee,self).__init__(firstName,surName,staffNumber, baseAnnualSalary, startDate)
       self.__hourlyRate__=hourlyRate
       self.__hoursWorked__=hoursWorked

    def calculatePay(self):
        #pay = hourWorked * hourlyRate
        pay = float(self.__hoursWorked__ * self.__hourlyRate__)
        return pay

    #super(B, self)
    def __str__(self):
        superStr = str(super(HourlyEmployee,self).__str__())

        return superStr + "\nHours Worked:" + str(self.__hoursWorked__) + "\nhourly rate: " + str(self.__hourlyRate__)

#COMMISION EMPLOYEE CLASS
class CommissionEmployee(Employee):
    #Attributes
    __commissionEarned__=0.00

    def __init__(self, firstName, surName, staffNumber, baseAnnualSalary, startDate, commissionEarned):
        super(CommissionEmployee,self).__init__(firstName, surName, staffNumber, baseAnnualSalary, startDate)
        self.__commissionEarned__ = commissionEarned

    def calculatePay(self):
        #pay = (baseAnnual / 12) + commissionEarned
        pay = float(self.__baseAnnualSalary__ / 12) + self.__commissionEarned__
        return pay

    def __str__(self):
        superStr = str(super(CommissionEmployee, self).__str__())

        return superStr + "\nCommission Earned:" + str(self.__commissionEarned__)





#main method
em1 = Employee('eric','strong',1,32500.00,'10/02/2017')
he1 = HourlyEmployee('laura','bermingham',2,0.00,'11/02/2017',40,10.50)
ce1 = CommissionEmployee('Dave','bermingham',3,50000.00,'12/02/2017',1000)

#printing out the objects
# print(em1)
# print("pay is " + str(em1.calculatePay()))
# print(he1)
# print("pay is " + str(he1.calculatePay()))
# print(ce1)
# print("pay is " + str(ce1.calculatePay()))

myEmployee = []

myEmployee.append(em1)
myEmployee.append(he1)
myEmployee.append(ce1)

for employee in myEmployee:
    print(employee)
    print("Pay is " + str(employee.calculatePay()))













