import numpy as np

class Die():
    def __init__(self, sides):
        self.sides = sides + 1
    def roll(self):
        return np.random.randint(1,self.sides)
