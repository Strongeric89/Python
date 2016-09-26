def toCypher(word,key):
    char = ''
    cypherText = ""

    # iterate through each character of the word
    for ch in word:
        # get the int value of the character
        enc = ord(ch) + key
        # get the character representation
        cypherText += chr(enc)
    return cypherText

def toPlain(word,key):
    char = ''
    plainText = ""

    # iterate through each character of the word
    for ch in word:
        # get the int value of the character
        enc = ord(ch) - key
        # get the character representation
        plainText += chr(enc)
    return plainText

#find out what the user wants
option = int(raw_input("[1]encrypt plaintext to cyphertext\n[2]decrypt cyphertext to plaintext\nuser:"))
if option == 1:
    word = raw_input("Enter a word: ")
    key = int(raw_input("enter a key: "))
    cypherText = toCypher(word,key)
    # just prints a line to divide up the output
    print("-" * 100)
    print("PlainText:\t" + word)
    print("CyperText:\t" + cypherText)

elif option ==2:
    word = raw_input("Enter a word: ")
    key = int(raw_input("enter a key: "))
    plainText = toPlain(word, key)

    # just prints a line to divide up the output
    print("-" * 100)
    print("PlainText:\t" + word)
    print("CyperText:\t" + plainText)

else:
    print("not a valid option.")


