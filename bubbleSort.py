import random
 
def randomGen():
    randomNumbers = []
    for x in range(20):
        randomNumbers.append(random.randint(0, 100))
    return randomNumbers

def bubbleSort(list):
    length = len(list)
    swapped = True
    for mainCounter in range(length):
        swapped = False
        for counter in range(length-1-mainCounter):
            if list[counter] > list[counter+1]:
                list = swap(list, (counter))
                swapped = True
        if swapped == False:
            print("sorted")
            return list
    return list
 
def swap(list, counter):
    temp = list[counter]
    list[counter] = list[counter+1]
    list[counter+1] = temp
    return list

randomNumbers = [5, 1, 4, 2, 8, 9]

sortedNumbers = bubbleSort(randomNumbers)
print("Sorted List : " + str(sortedNumbers))