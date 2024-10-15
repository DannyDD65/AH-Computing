import random
 
def randomGen():
    randomNumbers = []
    for x in range(10):
        randomNumbers.append(random.randint(0, 100))
    return randomNumbers

def insertionSort(list):
    value = 0
    index = 0
    for x in range(len(list)):
        value = list[x]
        index = x
        while index > 0 and value < list[index - 1]:
            list[index] = list[index - 1]
            index -= 1
        list[index] = value
    return list

for x in range(1):
    print(insertionSort(randomGen()))