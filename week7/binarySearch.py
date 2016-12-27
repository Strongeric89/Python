#the following program is binary Search
import random
def randomList():
    randomNumbers = []
    size = int(raw_input("How many Random Numbers? "))
    range = int(raw_input("what range of numbers (0-n)? "))

    counter = 0
    while(True):
        if(counter == size):
            break
        number = random.randint(0,range + 1)
        randomNumbers.append(number)
        counter += 1
    return randomNumbers

#binary search function
def binSearch(list):
    key = int(raw_input("Please specify a key to find: "))
    print("key: %d" % key)


    #bin Search algorithm
    low = 0
    high = len(list) - 1
    mid = (low + high) // 2

    while(low <= high):
        if list[mid] < key:
            low = mid + 1
        elif(list[mid] == key):
            print("found at index %d" % (mid + 1))
            break
        else:
            high = mid - 1

        high = (low + high) // 2

    if (low > high ):
        print("key not in the list")
        return 0

    # print("the number of steps taken : %d" % steps)


#main
#generate a random list of numbers
list = randomList()
list.sort()
i = 0
for num in list:
    print("index: %d\t value: %d" %(i,num))
    i+=1
index = binSearch(list)
if(index == 0 ):
    print("key is not in the list")
else:
    print("Key found at index %d" % (index))

