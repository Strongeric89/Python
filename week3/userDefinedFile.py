import time
## dd/mm/yyyy format

today = time.strftime("%d/%m/%Y")
print (today)
#the following program asks a user to name a file , put text in it and then asks to reopen to file

fileName = raw_input("Please name your File: ")
file = open(fileName, "a")
input = raw_input("Please enter what you want to enter to the file: ")
file.write(today + ":\t" + input + "\n")
print("writing to file......")
file.close()
prompt = raw_input("would you like to view what you wrote into the file?? [Y/N]")
if prompt == 'Y' or prompt == 'y':
    file = open(fileName)
    print(file.read())
    file.close()
elif prompt == 'N' or prompt =='n':
    print("Ok. ")
else:
    print("not a valid instruction")

