#File which will hold the implementation of the ships
# Created by Meagan Dyer 
#04/02/2023

class Ship:
    "Class Ship" 
    "Attributes: location, name and length"
    "Methods: getNumberofHits getlocation"

    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.hits = 0
        self.location = []
        self.sunk = False

    def getlength(self):
        return self.length
    
    #This function returns the location of the ship
    def getLocation(self):
        return self.location


    #This function returns the number of hits on the ship
    def getNumberofHits(self):
        return self.hits
    
    #This function returns the increase in hits on the ship 
    def HitIncrease(self):
       if self.sunk == False:
        self.hits = self.hits +1
        
        if self.hits == self.length:
            print(f"you have sunk the {self.name}")
            self.sunk = True





