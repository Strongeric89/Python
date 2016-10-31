"""The following program is to read from a file all of the words to a dictionary and their occurances.
Then must pipe over to a html document and print the occurances of the word relative to size in pixels.
"""
from string import punctuation
from collections import Counter

def getFile():
    file = open("Gettysberg.txt")
    text = file.read()
    return text

def stopWords():
    file = open("stopwords_en.txt")
    text2 = file.read()

    text2.replace('\n', ' ')
    words = text2.split(' ')
    return text2

def addToDict(text):
    words = ""
    text = text.replace('\n',' ')
    words = text.split(' ')

    for word in words:

        strip_punc(word)
        word.strip()
        word.lower()

    words.sort()
    return words

#removes all special characters
def strip_punc(s):
    return ''.join(c for c in s if c not in punctuation)

def noCommonWords(words,text2):
    #advanced part - check if the words list contains any common words. then add to another list.
    newWords = []
    for word in words:

        if word not in text2:
            newWords.append(word)

    return newWords

def newDictionary(words):
    #counting occurances of the word in a list and adding to a dictionary
    dict = Counter(words)

    for key,value in dict.items():
        print(key,value)

    return dict

def writeSpan(dict1,fileName):
    file2 = open(fileName,"a")
    basic = "<!DOCTYPE html><html><head lang=\"en\"><meta charset=\"UTF-8\"><title>Tag Cloud Generator</title></head><body><div style=\"text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black\">"
    file2.write(basic)
    for key,value in dict1.items():
        file2.write("<span style=\"font-size: {}px\"> {} </span>\n".format(value*10,key))
    file2.write("</div></body></html>")

#main flow

text = getFile()
#advanced part
text2 = stopWords()
words = addToDict(text)
#advanced part2

option = int(raw_input("Do you want\n[1]common words included\n[2]No common Words included\nUSER:"))
newWords = noCommonWords(words,text2)
if(option ==1):
    dict1 = newDictionary(words)
    writeSpan(dict1,"speech1.html")
elif(option ==2):
    dict1= newDictionary(newWords)
    writeSpan(dict1,"speech2.html")

print("Span tags have been writen to speech.html. There were %d elements created" % len(newWords))

