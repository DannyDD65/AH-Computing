import random
dogListInitiated = False

tournamentSize = int(input("How many dogs are entering the contest: "))
while tournamentSize < 1:
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
        print("Appended")

    def findNode(self, nodePlacement):
        current = self.head
        for x in range(nodePlacement):
            current = current.next
        return current
    
    def printList(self):
        current = self.head
        print("|Printing List|")
        while current:
            print(
                "Node: ", current,
                "\nName; ", current.data.name,
                "\nID: ", current.data.contestantID,
                "\nPoints: ", current.data.totalPoints,
                "\nNext: ", current.next
            )
            if current.next == None:
                return
            current = current.next

    def insertAtPoint(self, location, data):
        current = node(data)
        current.next = self.findNode(location)
        self.findNode(location-1).next = current

class dogList(linkedList):
    global tournamentSize
    def __init__(self, data):
        super().__init__(data)

    def insertAtPoint(self, location, data):
        current = node(data)
        current.next = self.findNode(location)
        self.findNode(location-1).next = current
    
    def findLastID(self):
        current = self.head
        while current.next is not None:
            current = current.next
        return current.data.contestantID

class dog:
    def __init__(self, loop):
        self.name = input("What is the dogs name: ")
        self.age = input("What is the dogs age: ")
        self.weight = input("How heavy is the dog: ")
        self.breed = input("What breed is the dog: ")
        self.ownersName = input("What is the Owners Name: ")
        print(dogList)
        if dogListInitiated != True:
            self.contestantID = 0
        else:
            self.contestantID = dogList.findLastID() + 1
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
    
dogList = dogList(dog(0))
dogListInitiated = True              #Boolean to check if dogList has been made to simplify extending of the list
for x in range(tournamentSize - 1):
    dogList.append(dog(x))

print("Tournament Size: " + str(tournamentSize))
dogList.append(dog(1))
print("Tournament Size: " + str(tournamentSize))

class round:
    def __init__(self, roundID):
        self.roundID = roundID

    def getRoundStats(self):
        print("Round Stats: " + str(self.roundID))

firstRound = round(1)
firstRound.getRoundStats()

for x in range(tournamentSize):
    print((dogList.findNode(x)).data.getName(), ": ", (dogList.findNode(x)).data.getPoints())
    print(x)

dogList.printList()