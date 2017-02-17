from Account import *  # importing the class


# depositAccount class
class DepositAccount(Account):
    # construct inheritance
    __interestRate__ = float(0.00)


    def __init__(self, accountName, accountNumber, sortCode, branchName, inCredit, acctBalance, interestRate):
        super(DepositAccount, self).__init__(accountName, accountNumber, sortCode, branchName, inCredit, acctBalance)
        self.__interestRate__ = interestRate
        self.__accType__ = "Deposit Account"


    # overriden methods
    def withdraw(self, deposited):
        print("You cannot withdraw from a deposit account")

    # overriden __str__
    def __str__(self):
        superStr = str(super(DepositAccount, self).__str__())

        return superStr + "\nInterest Rate :" + str(self.__interestRate__) + "%"
