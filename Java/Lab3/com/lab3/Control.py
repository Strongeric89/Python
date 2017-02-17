from Account import *
from DepositAccount import *
from CurrentAccount import *


#testing the objects
a1 = Account("eric",555,"bal606","balbriggan",True,100.50)
da1 = DepositAccount("Laura",666,"pal505","Palmerstown",True,700.10,21.5)
ca1 = CurrentAccount("Dave",777,"phib123","Phibsborough",True,1500.60,45.00)

#testing methods
a1.deposit(50)
a1.withdraw(200)

da1.withdraw(100)
da1.deposit(100)

ca1.withdraw(1500.00)
print ca1.checkCredit("mr. bermo")

a1.getDetails()
da1.getDetails()
ca1.getDetails()

a1.valuableAccount()
da1.valuableAccount()
ca1.valuableAccount()




