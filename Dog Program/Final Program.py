dogListInitiated = False #Boolean to check if dogList has been made to simplify extending of the list

def intChecker(inputMessage):
    toBeChecked = input(inputMessage)
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

    def getData(self):
        return self.data

class linkedList:
    def __init__(self, data):
        self.head = node(data)
        self.length = 1

    def getLength(self):
        return self.length

    def append(self, data):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node(data)
        self.length += 1

    def findNode(self, nodePlacement):
        while nodePlacement > (self.length - 1):
            nodePlacement = intChecker(str("Node doesnt exist, pick a node between 1 and " + str(self.length) + ": "))
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
        if location == 0:
            temp = self.head
            self.head = node(data)
            self.head.next = temp
        else:
            current = node(data)
            current.next = self.findNode(location)
            self.findNode(location-1).next = current
        self.length += 1

class dogList(linkedList):
    def __init__(self, data):
        super().__init__(data)

    def findMaxID(self):
        current = self.head
        maxID = current.data.contestantID
        while current.next is not None:
            current = current.next
            if current.data.contestantID > maxID:
                maxID = current.data.contestantID
        return maxID
    
    def searchList(self, searchInput):
        if searchInput == None:
            searchInput = intChecker("What is the dogID: ")
        current = self.head
        while int(current.data.contestantID) != int(searchInput):
            if current.next == None:
                print("|ERROR| DogID does not exist")
                dogList.searchList(input("What is the ID of the dog: "))
                return current.data
            current = current.next
        return current.data

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

class dog:
    def __init__(self):
        self.name = input("What is the dogs name: ")
        self.age = input("What is the dogs age: ")
        self.weight = input("How heavy is the dog: ")
        self.breed = input("What breed is the dog: ")
        self.ownersName = input("What is the Owners Name: ")
        if dogListInitiated != True:
            self.contestantID = 1
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
        return self.totalPoints
    
    def setName(self, value):
        self.name = value
    
    def setAge(self, value):
        self.age = value
    
    def setWeight(self, value):
        self.weight = value
    
    def setBreed(self, value):
        self.breed = value
    
    def setOwnersName(self, value):
        self.ownersName = value
    
    def getInformation(self):
        print("dogID: " + str(self.contestantID) + " | Name: " + str(self.name) + " | Age: " + str(self.age) + " | Weight: " + str(self.weight) + " | Breed: " + str(self.breed) + " | Owner's Name: " + str(self.ownersName))

class rounds:
    def __init__(self, roundID, activity):
        print("Round " + str(roundID) + " | " + activity)
        self.roundID = roundID
        self.activity = activity
        self.scores = linkedList(int(input("What is the dogID that came in 1st place: ")))
        dogList.searchList(self.scores.findNode(0).data).setPoints(5)
        self.scores.append(int(input("What is the dogID which came in 2nd place: ")))
        dogList.searchList(self.scores.findNode(1).data).setPoints(3)
        self.scores.append(int(input("What is the dogID which came in 3rd place: ")))
        dogList.searchList(self.scores.findNode(2).data).setPoints(2)
        for x in range(dogList.getLength()):
            if dogList.findNode(x).data.getContestantID() == self.scores.findNode(0).data or dogList.findNode(x).data.getContestantID() == self.scores.findNode(1).data or dogList.findNode(x).data.getContestantID() == self.scores.findNode(2).data:
                pass
            else:
                dogList.findNode(x).data.setPoints(1)

    def printScores(self):
        for x in range(self.scores.length):
            print(self.scores.findNode(x).getData())


tournamentSize = intChecker("How many dogs are entering the contest: ")

dogList = dogList(dog())
dogListInitiated = True #dogList has been initialised
for x in range(tournamentSize - 1):
    dogList.append(dog())

dogListFinished = False #Variable to decide when to exit the loop below and enter into the round phase of the program
while dogListFinished == False:
    for x in range(dogList.getLength()):
        dogList.findNode(x).data.getInformation()
    decision = input("Does this information look correct? Y/N: ").lower()
    if decision == "y":
        dogListFinished = True
    else: 
        print("What would you like to change?")
        modification = intChecker("Edit submissions - 1 | Add dog to list - 2 | Add dog in a certain location - 3 | Submit data - 4: ")
        while int(modification) < 1 or int(modification) > 4:
            print("|ERROR| Invalid Input")
            modification = intChecker("Edit submissions - 1 | Add dog to list - 2 | Add dog in a certain location - 3 | Submit data - 4: ")
        if modification == 1:
            modifiedDog = intChecker("What is the ID of the dog you would like to change: ")
            while modifiedDog > dogList.getLength():
                modifiedDog = intChecker("What is the ID of the dog you would like to change: ")
            print("What value would you like to change:")
            modifiedValue = intChecker("Name - 1 | Age - 2 | Weight - 3 | Breed - 4 | Owner's Name - 5: ")
            while modifiedValue > 5:
                print("|ERROR| Invalid input")
                modifiedValue = intChecker("Name - 1 | Age - 2 | Weight - 3 | Breed - 4 | Owner's Name - 5: ")
            if modifiedValue == 1:
                dogList.searchList(modifiedDog).setName(input("What is the dog's name: "))
            if modifiedValue == 2:
                dogList.searchList(modifiedDog).setAge(input("What is the dog's age: "))
            if modifiedValue == 3:
                dogList.searchList(modifiedDog).setWeight(input("What is the dog's weight: "))
            if modifiedValue == 4:
                dogList.searchList(modifiedDog).setBreed(input("What is the dog's breed: "))
            if modifiedValue == 5:
                dogList.searchList(modifiedDog).setOwnersName(input("What is the owner's name: "))
        elif modification == 2:
            dogList.append(dog())
        elif modification == 3:
            placement = intChecker("What place would you like to place the dog: ")
            while placement > dogList.getLength():
               placement = intChecker("What place would you like to place the dog: ")
            dogList.insertAtPoint((placement - 1), dog())
        elif modification == 4:
            dogListFinished = True

# roundList = linkedList(rounds(1, "running"))
# roundList.append(rounds(2, "jumping"))
# roundList.append(rounds(3, "galoping"))
# roundList.append(rounds(4, "singing"))

dogList.printList()

# for x in range(dogList.getLength()):
#     print((dogList.findNode(x)).data.getName(), ": ", (dogList.findNode(x)).data.getPoints())