class Animal:

    def __init__(self, species, name):
        self.species = species
        self.name    = name
        self.alive   = True

    def __str__(self):
        return "{} is a {}".format(self.name, self.species)




    # getters and setters

    def getSpecies(self):
        return self.species

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name
