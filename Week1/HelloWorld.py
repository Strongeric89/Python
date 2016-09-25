"""the following program is lab 1 week 1 a simple hello world programm"""
def hello(name):
    newName = "Hello " + name
    print(newName)

name=raw_input("Please enter your name:")
#calling the method to print the name
hello(name)

