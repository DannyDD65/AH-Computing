import random
 
def randomGen():
    randomNumbers = []
    for x in range(20):
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

def binarySearch(list, target):
    low = 0
    high = len(list)
    mid = 0
    found = False
    while found == False and low <= high:
        mid = int((low+high)/2)
        if target == list[mid]:
            return ("Found at position " + str(mid + 1))
        elif target > list[mid]:
            low = mid + 1
        else:
            high = mid-1
    if found == False:
        return "Targer not found"
    
numbers = insertionSort(randomGen())

displayNumbers = "list of numbers: " + str(numbers[0])
for x in range(len(numbers)-1):
    displayNumbers += ", " + str(numbers[x+1])
print(displayNumbers)

target = int(input("What number are you looking for: "))
while target not in numbers:
    target = int(input("What number are you looking for: "))

print(binarySearch(numbers, target))