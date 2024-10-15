class dog:
    def __init__(self, name, colour, height, length, weight, breed):
        self.name = name
        self.colour = colour
        self.height = height
        self.length = length
        self.weight = weight
        self.breed = breed

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getColour(self):
        return self.colour
    
    def setColour(self, colour):
        self.colour = colour

    def getHeight(self):
        return self.height
    
    def setHeight(self, height):
        self.height = height

    def getLength(self):
        return self.length
    
    def setLength(self, length):
        self.length = length

    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        self.weight = weight

    def getBreed(self):
        return self.breed
    
    def setBreed(self, breed):
        self.breed = breed

class policeDog(dog):
    def __init__(self, name, colour, height, length, weight, breed, policeID, handler):
        super().__init__(name, colour, height, length, weight, breed)
        self.policeID = policeID
        self.handler = handler

    def getPoliceID(self):
        return self.policeID
    
    def setPoliceID(self, policeID):
        self.policeID = policeID

    def getHandler(self):
        return self.handler
    
    def setHandler(self, handler):
        self.handler = handler

class sheepDog(dog):
    def __init__(self, name, colour, height, length, weight, breed):
        super().__init__(name, colour, height, length, weight, breed)

        def getBreed(self):
            if self.breed == True:
                return "Border Collie"
            else:
                return "Unknown"

Rex = dog("Rex", "Black", 60, 80, 140, "Labrador")

Sarge = policeDog("John", "Black", 60, 80, 140, "Labrador", 10, "Pete")

mary = sheepDog("Mary", "Golden", 50, 60, 120, True)

#Sarge.setName("Sarge")
#Sarge.setColour("Black")
#Sarge.setHeight(120)
#Sarge.setLength(150)
#Sarge.setWeight(250)
#Sarge.setBreed("Alsatian")

#print(Sarge.getName())
#print(Sarge.getColour())
#print(Sarge.getHeight())
#print(Sarge.getLength())
#print(Sarge.getWeight())
#print(Sarge.getBreed())
#print(Sarge.getPoliceID())
#print(Sarge.getHandler())

print(mary.getBreed())
mary.setBreed(False)
print(mary.getBreed())