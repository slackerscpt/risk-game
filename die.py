import numpy as np

class Die():
    def __init__(self, sides):
        self.sides = sides
    def roll(self):
        return np.random.randint(1,self.sides)
