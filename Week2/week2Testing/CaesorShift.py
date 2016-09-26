#the following program is to produce a caeser shift
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

key = int(raw_input("enter a key:"))
phrase = raw_input("enter a phrase to encrypt: ")
character = ''
cipherText = ''
for i in phrase:
    index = letters.index(i)


