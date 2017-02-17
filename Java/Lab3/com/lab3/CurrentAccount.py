from Account import * #import methods
class CurrentAccount(Account):

    __penaltyAmmount__=float(20.00)

    def __init__(self,accountName, accountNumber,sortCode,branchName,inCredit,acctBalance, penalty):
        super(CurrentAccount, self).__init__(accountName, accountNumber,sortCode,branchName,inCredit,acctBalance)
        self.__penaltyAmmount__=penalty
        self.__accType__= "Current Account"

    #overriden withdraw method
    def withdraw(self, deposited):
        #checking if operation is allowed
       bal = self.__acctBalance__ - deposited
       if(float(bal) <= 0.00):
           print("Insufficient Funds")
       else:
           self.__acctBalance__ -= deposited
           print("You have withdrawn " + str(deposited) + "\nYour balance is " + str(self.__acctBalance__))


    #overloaded methods
    def checkCredit(self):
        if(self.__inCredit__ == True):
            return "You are in Credit."
        else:
            return "You are not in Credit"

    def checkCredit(self, warning):
        if(self.__acctBalance__ < 100.00 and self.__acctBalance__ > 0.00):
            return warning + ": your account is less than 100 and greater than 0"
        else:
            return "non applicable"

    def __str__(self):
        superStr = str(super(CurrentAccount, self).__str__())

        return superStr + "\nPenalty Charge : " + str(self.__penaltyAmmount__)










