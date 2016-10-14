#the following program takes in a string and concats a new string to the end of the file
def getFile():
    isRunning = True
    while(isRunning):
        try:
            file = open("students.txt")
        except IOError:
            print("File Could not be found")
            isRunning = True
        else:
            isRunning = False
            return file

def addExt(file):
    #add the @mydit.ie onto every email
    extension = "@mydit.ie"
    studentList = []
    newList = []
    studentList = file.readlines()
    #studentList.append(file.split('\n'))
    for student in studentList:
        student = student.replace("\n",extension)
        student = student + "," + "\n"
        #print(student)
        newList.append(student)


    return newList


def writeFile(list):
    newFile = open("studentsEmail.txt","a")
    for student in list:
        newFile.write(str(student))

    file.close()






file = getFile()
#add emailExt onto list
list = addExt(file)
writeFile(list)

