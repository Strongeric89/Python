#the following program is for lab week 3 a palidrome checker
userWord = raw_input("Enter your Word: ")
space = ' '
coma = '\''
hiphan = ','
#convert to lowercase
userWord = userWord.lower()
print("[1]- convert to lowercase \tyour word is now: {:2s}".format(userWord))



#new array to contain characters
noSpaceWord = []
newWord =''
for ch in userWord:
    #get rid of spaces
    if ch == space or ch ==coma or ch ==hiphan:
        continue
    else:
        noSpaceWord += ch



for ch in noSpaceWord:
    newWord += ch

print("[2]-remove spaces and coma's \t\tyour word is now: " + newWord)
#remove whitespace
userWord = userWord.strip()
print("[3]- remove any whitespace \t\tyour word is now: {:2s}".format(newWord))

#reverse the word and check
userWordReversed = newWord[::-1]
print("[3]- reverse the word and check\t\tyour word is now: {:2s}".format(userWordReversed))

if(newWord == userWordReversed):
    print("\n\nthe word {} is a Palindrome!".format(newWord))
else:
    print("\n\nthe word {} is NOT a Palindrome!".format(newWord))







