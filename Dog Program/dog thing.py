def initiateShow():
    noDogs = int(input("How many dogs are entering"))
    while isinstance(noDogs, int) == False:
        noDogs = input("How many dogs are entering")
    dogList = [] * noDogs

class dog:
    def __init__(self, age, weight, breed, ownersName, contestantID):
        self.age = age
        self.weight = weight
        self.breed = breed
        self.ownersName = ownersName
        self.contestantID = contestantID
        self.totalPoints = 0

    def getPoints(self):
        return self.totalPoints
    
dogList = []
    
for x in range(3):
    dogList.append(dog(input("What is the dogs age,"), input("How heavy is the dog"), input("Can i breed it"), input("Can i breed you"), input("Just like the nazis, whats your number")))