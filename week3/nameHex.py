name = raw_input("Enter your name: ")
name = name[::-1]
string = ''
for ch in name:
    dec = ord(ch)


    #array of numbers to show the index of the new number
    numbers = [1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    #algorithm to get the hex version

    while dec > 0:
        r = int(dec % 16)
        dec = dec // 16

        if r > 9:
            string = str(numbers[r-1])+ string
        else:
            string = str(r) + string

print("0x"+ string)
