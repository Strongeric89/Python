import string
#the folloprogram is used to find a e i o u in a dictionary file
def findTheVowels(file):
    vowels = ['a','e','i','o','u']
    words = []
    #read in line by line
    for line in file:
        word = line.strip()
        for ch in word:
            for letter in vowels:
                if ch == letter:
                    #print(word)
                    words.append(word)
    return words



def readFile():
    isRunning = True
    while(isRunning):
        nameOfFile = raw_input("please enter a the filename:  ")
        try:
            file = open(nameOfFile)
        except IOError:
            print("file not found!")
            isRunning = True
        else:
            print("file located and found")
            isRunning = False

#call the findTheVowels Function

    words = findTheVowels(file)
    return words

#set up the file
print("dictionary APP")
checkedWords = []
words=readFile()
seq = "aeiou"
inWord = ""
i = 1
print(len(words))
#get each individual word
for word in words:
    word = word.strip()
    if len(word) <=6:
        continue

    for char in word:
        if char in seq:
            inWord += char

    if inWord == seq:
        print(inWord)







