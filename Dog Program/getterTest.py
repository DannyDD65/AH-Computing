import random

dogListInitiated = False #Boolean to check if dogList has been made to simplify extending of the list

def intChecker(inputMessage, toBeChecked):
    while True:
        try: #checks if dateBeingChecked is an integer and is above 0
            if int(toBeChecked) >= 1:
                toBeChecked = int(toBeChecked) #sets dataBeingChecked to an integer instead of the string form it starts with
                return toBeChecked #breaks out of the while loop
            print("|HAS TO BE AN INTEGER ABOVE 0|")
            toBeChecked = input(inputMessage) 
        except: #if it is not an integer, the above code returns an error and runs this piece instead
            print("| HAS TO BE INTEGER ABOVE 0|")
            toBeChecked = input(inputMessage) 

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, data, length):
        self.head = node(data)
        self.length = length

    def getLength(self):
        return self.length

    def append(self, data):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node(data)
        self.length += 1

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
                "\nData ", current.data,
                "\nNext: ", current.next
            )
            if current.next == None:
                return
            current = current.next

    def insertAtPoint(self, location, data):
        current = node(data)
        current.next = self.findNode(location)
        self.findNode(location-1).next = current
        self.length += 1

class dogList(linkedList):
    def __init__(self, data, length):
        super().__init__(data, length)

    def append(self, data):
        return super().append(data)

    def insertAtPoint(self, location, data):
        current = node(data)
        current.next = self.findNode(location)
        self.findNode(location-1).next = current
        self.length += 1
    
    def findMaxID(self):
        current = self.head
        maxID = current.data.contestantID
        while current.next is not None:
            current = current.next
            if current.data.contestantID > maxID:
                maxID = current.data.contestantID
        return maxID
    
    def searchList(self, searchInput):
        current = self.head
        while current.data.contestantID != searchInput:
            current = current.next
            if current.next == None:
                print("|ERROR| DogID does not exist")
                return
        return current.data.contestantID

    def printList(self):
        current = self.head
        print("|Printing Dog List|")
        while current:
            print(
                "Node: ", current,
                "\nName :", current.data.name,
                "\nID :", current.data.contestantID,
                "\nPoints :", current.data.totalPoints,
                "\nNext: ", current.next
            )
            if current.next == None:
                return
            current = current.next

class roundList(linkedList):
    def __init__(self, data, length):
        #while data =
        self.head = node(data)
        self.length = length

class dog:
    def __init__(self):
        self.name = input("What is the dogs name: ")
        self.age = input("What is the dogs age: ")
        self.weight = input("How heavy is the dog: ")
        self.breed = input("What breed is the dog: ")
        self.ownersName = input("What is the Owners Name: ")
        if dogListInitiated != True:
            self.contestantID = 0
        else:
            self.contestantID = dogList.findMaxID() + 1
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
    
tournamentSize = intChecker("How many dogs are entering the contest: ", input("How many dogs are entering the contest: "))

dogList = dogList(dog(), 1)
dogListInitiated = True              #dogList has been initialised
for x in range(tournamentSize - 1):
    dogList.append(dog())

class rounds:
    def __init__(self, roundID):
        self.roundID = roundID
        self.scores = linkedList(input("What was " + dogList.findNode(0).data.getName() + "'s score: "), 1)
        for x in range(tournamentSize-1):
            self.scores.append(input("What was " + dogList.findNode(x+1).data.getName() + "'s score: "))

    def printScores(self):
        self.scores.printList()

    # def getRoundStats(self):
    #     print("Round Stats",
    #           "\nRound ID: ", self.roundID,)

for x in range(dogList.getLength()):
    print((dogList.findNode(x)).data.getName(), ": ", (dogList.findNode(x)).data.getPoints())

roundList = linkedList(rounds(0), 1)
roundList.findNode(0).data.printScores()

dogList.printList()