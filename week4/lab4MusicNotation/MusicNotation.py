
#the following ptrogram reads from a file and extracts information based on keys

#extract keys from file
def getKeys(file):

    words = []
    id = []
    title = []
    time = []
    key = []

    #getting each individual line into an array seperated by lines
    for line in file:
        words.append(line)

    size = 0

    for ch in words:

        if (ch.__contains__('X:')):
            ch = ch[2:-1]
            id.append(ch)
            size += 1

        if (ch.__contains__('K:')):
            ch = ch[2:-1]
            key.append(ch)

        if(ch.__contains__('T:')):
            ch = ch[2:-1]
            title.append(ch)

        if (ch.__contains__('M:')):
            ch = ch[2:-1]
            time.append(ch)
    #print("There are " + str(len(title) + "in the file")

    for i in range(0,size):

        print(str(id[i]) + " ..." + str(title[i]) + "..." + str(time[i]) + "..." + str(key[i]))


    return len(title)

#get the file
def getFile():
    file = open("hnr.abc")
    #print(file.read())
    return file


#main program flow

file = getFile()
print("--ABC Music Notation --")
num = getKeys(file)
print("There are " + str(num) + " songs in the file")

