#the following program is a test example on how to use File IO in Python
print("File IO Example!")
#to open a file
#STEP 1
fileTest = open("test.txt")
#STEP 2
#to Read file
print(fileTest.read())

#STEP 3
#get pointer position
position = fileTest.tell()
print("Position of the pointer is " + str(position))


#reset the pointer to the beginning
position = fileTest.seek(0,0)

#reprint the file
print(fileTest.read())

#close the file when finished
fileTest.close()
