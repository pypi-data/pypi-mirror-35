from Animal import *

class Owl(Animal):

    def __init__(self, name, sound):
        Animal.__init__(self, species="Owl", name=name)
        self.speak = sound




    # getters
    def getSound(self):
        return self.speak
