"""
the following program is for Lab Test 1, Semester 1, Python
Author: Eric Strong C15708709
Date: 27/10/2016
Description: a library book system implementing dictionaries and functions
Version: Python 2.7.11
Platform: Windows 10, PyCharm Community Edition 2016.2.3
NOTE: due to my version of python I can only use raw_input() instead of input() to read in from std input
"""
#function to add a book
def addBook():

    #error checking
    isRunning = True
    while(isRunning):

        #add new book to existing list
        isbn = raw_input("please enter the ISBN: ")
        if(len(isbn) > 12):
            break
        else:
            print("The isbn must contain 13 digits. eg 1234567890000")

    isbn = int(isbn)
    title = raw_input("Please enter the title of the book: ")
    title = title.lower()
    author = raw_input("Please enter the Author of the Book:")
    author = author.lower()

    #error checking to stop a letter being entered
    while(isRunning):
        try:
            quantity = int(raw_input("Please enter the quantity of the book: "))
            isRunning = False
        except ValueError:
            print("Please enter a digit.")
            isRunning = True


    for key, value in existingBooks.items():
        if(isbn == key):
            #change quantity
            quantity = value[2] + quantity

    newBook = [title, author, quantity]
    #implementing the structure
    existingBooks.update({isbn:newBook})

def displayAll():
    si=" ISBN:"
    ti="TITLE:"
    au="AUTHOR:"
    qu="QUANTITY:"
    print("{:15}\t|{:20}\t|{:20}\t|{}".format(si,ti,au,qu))
    print("-"*73)
    # print all of the books
    for key, value in existingBooks.items():
        print("{:15}\t|{:20}\t|{:20}\t|{}".format(key, value[0],value[1],value[2]))

def checkBook():
    #checking out a book will effect the quantity
    book = raw_input("what book do you want to check out? ")
    book = book.lower()
    number = 0

    for key, value in existingBooks.items():
        if(book == value[0]):
            print("checking out %s" %(value[0]))
            #change quantity
            value[2] -= 1
            number = 1

    if (number == 0):
        print("%s is not available at this moment" % book)


def search():
    #search for a book by title and return ISBN
    book = raw_input("what book do you want to search for? ")
    book = book.lower()
    number = 0
    for key, value in existingBooks.items():
        if (book == value[0]):
            print("ISBN: %d" % (key))
            number = 1
            break

    if (number == 0):
        print("%s is not available at this moment" % book)

def merge():
    #function to merge the libraries
    print("Merging Libraries...")
    listToMerge = {1234567890001: ["the book1", "mr.blog", 1], 1234567890007: ["the book7", "john.blog", 4],
                     1234567890009: ["the book9", "dr.Python", 4]}


    for key,value in existingBooks.items():
       for key2,value2 in listToMerge.items():
            if (key == key2):
                quantity = value[2]
                # change quantity
                value[2] = value2[2] + quantity
                listToMerge.update({key:value})
       existingBooks.update(listToMerge)

#main
print("Welcome to the Library Book System.")

#part (a)
#dictionary pair with an id and list containing name, author and quantity
existingBooks = {1234567890001:["the book1", "mr.blog",1],1234567890002:["the book2", "ms.blog",2],1234567890003:["the book3", "sir.blog",3]}
isRunning = True
isRunning2=True
while(isRunning):
    while(isRunning2):
        try:
            option = int(raw_input("\n[1]Display Books\n[2]Add a book\n[3]Check out a book\n[4]Search for a Book\n[5]Merge Libraries\n USER: "))
            break
        except ValueError:
            print("not a valid type. again")
            isRunning2=True

    if(option == 1):
        #call display function
        displayAll()

    elif (option == 2):
        #call add a book
            addBook()
    elif (option ==3):
        #call check out a book
        checkBook()
    elif (option == 4):
        #call search for book by title
        search()
    elif (option == 5):
        #call merge Libraries
        merge()
    else:
        print("not a valid option try again")