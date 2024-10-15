import random

tournamentSize = int(input("How many dogs are entering the contest: "))

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, data):
        self.head = node(data)

    def append(self, data):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node(data)

    def findNode(self, nodePlacement):
        current = self.head
        for x in range(nodePlacement):
            current = current.next
        return current
    
    def printList(self):
        current = self.head
        while current:
            print(
                "Node: ", current,
                "\nName; ", current.data.name,
                "\nID: ", current.data.contestantID,
                "\nPoints: ", current.data.totalPoints,
                "\nNext: ", current.next
            )
            current = current.next

    def insertAtPoint(self, location, data):
        current = node(data)
        current.next = self.findNode(location)
        self.findNode(location-1).next = current
        print(data.name, " ", current.next.data.name, " ", self.findNode(location-1).next.data.name)

class dog:
    def __init__(self, loop):
        self.name = input("What is the dogs name: ")
        self.age = input("What is the dogs age: ")
        self.weight = input("How heavy is the dog: ")
        self.breed = input("What breed is the dog: ")
        self.ownersName = input("What is the Owners Name: ")
        self.contestantID = loop
        self.totalPoints = 0

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getWeight(self):
        return self.weight

    def getBreed(self):
        return self.breed

    def getOwnersName(self):
        return self.ownersName

    def getContestantID(self):
        return self.contestantID

    def getPoints(self):
        return self.totalPoints
    
    def setPoints(self, value):
        self.totalPoints += value
    
dogList = linkedList(dog(0))
for x in range(tournamentSize - 1):
    dogList.append(dog(x))

dogList.insertAtPoint(1, dog(2))
tournamentSize += 1

# def round(tournamentSize, measurement):
#     if measurement == 0:
#         winner = random.randint(0, tournamentSize-1)
#         (dogList.findNode(winner)).data.setPoints(5)
#     if measurement == 1:
#         rankedList()

class round:
    def __init__(self):
        pass

round(tournamentSize, None)

for x in range(tournamentSize):
    print((dogList.findNode(x)).data.getName(), ": ", (dogList.findNode(x)).data.getPoints())
    print(x)

dogList.printList()