#populating an array from a users input
print("Populating arrays.....")
size = int(raw_input("How many elements in the array?"))
array1 = []
for i in range(0,size):
    x = int(raw_input("element #" + str(i) + ":\t"))
    array1.append(x)

print("the max value of the array is %s" % max(array1))
print("the min value of the array is " + str(min(array1)))
print("the sum of the array is " + str(sum(array1)))

print("sorting array.....")
#using sort function
print("sorted array1: %s" % sorted(array1))
