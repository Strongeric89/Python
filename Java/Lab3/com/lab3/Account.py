#super class
class Account(object):

    #attributes
    __accountName__ = ""
    __accountNumber__ = int(1)
    __sortCode__ = ""
    __branchName__ = ""
    __inCredit__ = bool(True)
    __acctBalance__ = float(0.00)
    #part 4


    __accType__ = ""

    def __init__(self,accountName, accountNumber,sortCode,branchName,inCredit,acctBalance):



        self.__accountName__ = accountName
        self.__accountNumber__= accountNumber
        self.__sortCode__ = sortCode
        self.__branchName__= branchName
        self.__inCredit__=bool(inCredit)
        self.__acctBalance__=float(acctBalance)
        self.__accType__= "Account"

        print(str(self.__accountNumber__) +  " " + self.__accountName__ + " account created")



    def deposit(self, deposited):
        self.__acctBalance__ += float(deposited)
        print("you have deposited " + str(deposited) + "\n your balance is now " + str(self.__acctBalance__))


    def withdraw(self, deposited):
        self.__acctBalance__ -= float(deposited)
        print("you have withdrawn " + str(deposited) + "\n your balance is now " + str(self.__acctBalance__))


    def __str__(self):
        return "Name: " + str(self.__acctBalance__) + "\nAccount Number: " + str(self.__accountNumber__) + "\nSort Code: " + str(self.__sortCode__) + "\nBranch Name: " + str(self.__branchName__) + "\n in Credit: " + str(self.__inCredit__) + "\nAccount Balance: " + str(self.__acctBalance__)

    def getDetails(self):
        print("\nAccount type: " + self.__accType__ + "\nAccount Balance: " + str(self.__acctBalance__) + "\nAccount Name: " + self.__accountName__)

    def valuableAccount(self):
        print("The balance of the account is : " + str(self.__acctBalance__))

