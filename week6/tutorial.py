#the folowing program is used as a shopping app
"""the functionality of the app is to add, remove, check price, check description """

#add item to the dictionary - description and price pair
#
# def goToAdd():
#     option = raw_input("would you like to add items?[Y/N]")
#     if option == 'Y' or 'y':
#         addItem(shopItems)
#         return 0
#     elif option == 'n' or 'N':
#         return 0
#     else:
#         print("not a valid option")
#         return 0

def checkLen(shopItems):
    if len(shopItems) < 1:
        print("There are no Items in the Shop List!")


#check price function
def checkPrice(shopItems):
    checkLen(shopItems)
    item = raw_input("what item to get price on?")
    item = item.lower()

    #find the item
    euro = '\xe2\x82\xac'
    for key,value in shopItems.items():
        if item == key :
            print("the price of {} is {}{:.1f}".format(item, euro,value))
            break
    else:
        print("The item %s is not in the shop list" %item)

def addItem(shopItems):
    euro = '\xe2\x82\xac'
    itemToAdd = raw_input("enter Item Description: ")
    itemToAdd = itemToAdd.lower()
    itemPrice = float(raw_input("enter Item Price:" + euro + " "))

    # check if the item already exists
    for key, value in shopItems.items():
        if itemToAdd == key:
            print("{} already exists in the list".format(itemToAdd))
            break
    else:
        shopItems.update({itemToAdd: itemPrice})
        print("%s added to the list" % (itemToAdd))

    return shopItems

#check price function
def delItem(shopItems):
    checkLen(shopItems)
    item = raw_input("what item to delete?")
    item = item.lower()
    #find the item
    for key,value in shopItems.items():
        if item == key :
            shopItems.pop(item)
            print("{} was removed from the list".format(item))
            break
    else:
        print("The item %s is not in the shop list" %item)

#printing the entire dictionary
def displayAll(shopItems):
    checkLen(shopItems)
    #display the entire dictionary
    print("Price:\tDescritpion:")
    print("*"*30)
    euro = '\xe2\x82\xac'

    for key,value in shopItems.items():
        print("{} {:.2f} | \t {}".format(euro,value,key))

#main

#global dictionary
shopItems = {}
euro = '\xe2\x82\xac'

isRunning= True
isRunning2=True
while(isRunning):

    #for input
    while(isRunning2):

        #print("\n" * 3)
        print("*" * 30)
        try:
            option = int(raw_input("Please select an option:\n[1]Add item to Shop\n[2]Remove Item from Shop\n[3]Check Price on Item\n[4]Get Display all products\n\nUSER: "))
            print("\n"*5)
            break
        except ValueError:
            print("try again")
            isRunning2=True

    if(option == 1):
        print("Add Item>>")
        addItem(shopItems)
    elif (option == 2):
        print("Remove Item>>")
        delItem(shopItems)
    elif (option == 3):
        print("check price on item>>")
        checkPrice(shopItems)
    elif (option == 4):
        print("Display all products>>")
        displayAll(shopItems)
    elif(option == 0):
        print("exiting>>")
        isRunning = False
    else:
        print("not a valid option. Try again!")