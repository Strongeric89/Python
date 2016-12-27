user_word = raw_input("enter a word: ")
encrypted=''

for ch in user_word:
    encLetter = ord(ch) + 1
    encrypted += chr(encLetter)

print(encrypted)
