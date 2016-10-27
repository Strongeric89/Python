#the following program is sequential Search
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

#sequential search function
def seqSearch(list):
    key = int(raw_input("Please specify a key to find: "))
    print("key: %d" % key)

    #Sequential Search algorithm
    index = 0
    steps = 0
    for num in list:
        steps += 1
        if(num == key):
            index = list.index(num)
            break

    if(index == 0):
        print("key %d is not in the list" % key)
    else:
        print("Key %d found at index %d" % (key,index))

    return steps



#main
#generate a random list of numbers
list = randomList()
i = 0
for num in list:
    print("index: %d\t value: %d" %(i,num))
    i+=1
steps = seqSearch(list)
print("The number of steps used are : %d" % steps)