#the folowing program is used as a shopping app
"""the functionality of the app is to add, remove, check price, check description """

def checkLen(shopItems):
    if len(shopItems) < 1:
        print("There are no Items in the Shop List!")
        return False
    else:
        return True

def expensive(shopItems):
    largest = 0.00
    winner = ""

    check = checkLen(shopItems)
    if check == True:
        for key,value in shopItems.items():
            if value > largest :
                largest = value
                winner = key

        print("The Largest Item in the Basket is {} {}{:.2f}".format(winner,euro,largest))
        #pair = (largest,winner)
        #return pair


    else:
        print("")
        return 0.00


#check price function
def checkPrice(shopItems):

    check =checkLen(shopItems)
    if check == True:

        item = raw_input("what item to get price on?")
        item = item.lower()
        print("please enter an item, not a value.")


        #find the item
        euro = '\xe2\x82\xac'
        for key,value in shopItems.items():
            if item == key :
                print("the price of {} is {}{:.2f}".format(item, euro,value))
                break
        else:
            print("The item %s is not in the shop list" %item)
    else:
        print("")

def addItem(shopItems, total):
    euro = '\xe2\x82\xac'
    isRunning1=True

    itemToAdd = raw_input("enter Item Description: ")
    itemToAdd = itemToAdd.lower()

    while(isRunning1):
        try:
            itemPrice = float(raw_input("enter Item Price:" + euro + " "))
            break
        except ValueError:
            print("please enter Value only. {:}0.00".format(euro))
            isRunning1=True

    total = total + itemPrice
    # check if the item already exists
    for key, value in shopItems.items():
        if itemToAdd == key:
            print("{} already exists in the list".format(itemToAdd))
            break
    else:
        shopItems.update({itemToAdd: itemPrice})
        print("\n%s added to the list" % (itemToAdd))

    return total

#check price function
def delItem(shopItems,total):
    check =checkLen(shopItems)
    if check == True:
        item = raw_input("what item to delete?")
        item = item.lower()
        #find the item
        for key,value in shopItems.items():
            if item == key :
                shopItems.pop(item)
                if(total == 0.00):
                    break
                else:
                    total = total - value
                    print("{} was removed from the list".format(item))
                    return total
                    break
        else:
            print("The item %s is not in the shop list" %item)
    else:
        print("")

#printing the entire dictionary
def displayAll(shopItems):
    check=checkLen(shopItems)
    if check == True:

        #display the entire dictionary
        print("Price:\tDescritpion:")
        print("*"*30)
        euro = '\xe2\x82\xac'

        for key,value in shopItems.items():
            print("{} {:.2f} | \t {}".format(euro,value,key))

    else:
        print(" ")



#main

#global dictionary
total = 0.00
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
            option = int(raw_input("Please select an option:\n[1]Add item to Shop\n[2]Remove Item from Shop\n[3]Check Price on Item\n[4]Get Display all products\n[5]Display Total\n[6]Most Expensive Item in the Basket\n\nUSER: "))
            print("\n"*5)
            break
        except ValueError:
            print("try again")
            isRunning2=True

    if(option == 1):
        print("Add Item>>")
        total = addItem(shopItems,total)
    elif (option == 2):
        print("Remove Item>>")
        total = delItem(shopItems,total)
    elif (option == 3):
        print("check price on item>>")
        checkPrice(shopItems)
    elif (option == 4):
        print("Display all products>>")
        displayAll(shopItems)
        if(total > 0.00):
            print("-"*30)
            print("{} {:.2f} | \tSUBTOTAL".format(euro, total))

    elif(option == 0):
        print("exiting>>")
        print("Thank you for using the Shopping List app. Goodbye")
        isRunning = False
    elif(option ==5):
        print("Your total Basket is {}{:.2f}".format(euro,total))
    elif (option == 6):

        expensive(shopItems)

    else:
        print("not a valid option. Try again!")