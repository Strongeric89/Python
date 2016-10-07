import string
#opening the file
def openFile():
    isRunning = True
    while(isRunning):
        nameFile = raw_input("Enter the name of the file: ")
        try:
            file = open(nameFile)

        except IOError:
            print("not a valid file")
            isRunning = True
        else:
            print("opening file...............")
            text = file.read()
            isRunning = False
    input= raw_input("Would you like to view original file? [Y/N]")

    if(input == 'y' or input == 'Y'):
        print(text)
        return text

    elif(input == 'n' or input == 'N'):
        print("ok.")
        return text

    else:
        print("not a valid option. take it as no")
        return text



#jumble algorithm
def jumble(word):
    # first and last
    firstLet = word[0]
    size = len(word)
    lastLet = word[(size - 1)]

    testWord = word[1:size]
    newSize = size - 1
    testWord = testWord[0:newSize - 1]

    newWord = ""
    # print(testWord)
    newSize = len(testWord)

    for i in range(newSize):
        if (i % 2 == 0):
            newWord = testWord[i] + newWord
        if (i % 2 == 1):
            #newWord += testWord[i]
            newWord = testWord[i] + newWord

    # add back the first and last
    jumbled = firstLet + newWord + lastLet
    return jumbled

#get each word from the text string
def getWord(text):
    # get individual words
    words = text.split(' ')
    jumbledWords = []

    # iterate through each word and jumble them
    for word in words:
        jumbledWord=jumble(word)
        jumbledWords.append(jumbledWord)
    return jumbledWords


#main program

text = openFile()
allJumbledUp = getWord(text)
print("jumbling up text.......................\n")
for i in allJumbledUp:
    print(i)

