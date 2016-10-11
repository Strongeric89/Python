import random
#the following program is a bubble sort algorithm

def randomList():
    loop = True
    while(loop):
        try:
            seq = int(raw_input("How many random numbers do you want? "))
        except ValueError:
            print("Not a valid number. Try again!")
            loop = True
        else:
            loop = False
            randomNumbers = []
            isRunning = True
            i = 0
            while(isRunning):
                if(i == seq):
                    break
                else:
                    randomNumbers.append(random.randint(0,100))
                    i +=1
    return randomNumbers


def bubbleSort(list):
    size = len(list)
    steps = 0

    for i in range(0,size):
        for j in range(0,size -i -1):
            if(list[j] > list[j + 1]):
                temp = list[j]
                list[j] = list[j + 1]
                list[j+1] = temp
                #counter for steps in the algorithm
                steps +=1
    print("the number of steps to sort: " + str(steps))
    return list


list = randomList()
print("Generating Numbers.................................")
print("\n\nThe unsorted List: " + str(list))
sortedList = bubbleSort(list)
print("\n\nThe sorted List: " + str(sortedList))







