#the following program creates a file in python
fileName = "batman.txt"
file = open(fileName,"a")
print("Writing to file " + fileName)
file.write("Story bud This is a program that writes new stuff\n\nhell year!")
file.close()

#now open the file
file = open(fileName)
print(file.read())