print("The following program simulates file IO with exceptions")


isRunning = True
while(isRunning):
    fileName = raw_input("enter the name of file: ")
    try:

        file = open(fileName)
    except IOError:
        print(fileName + " not found. Try again!")
        isRunning = True
    else:
        print("-" * 50)
        print("FILE:")
        print(file.read())
        isRunning = False

print("file was opened successfully and read.")
