"""
coin.py
Joel Bratt
make a coin class for use in the main py
6/24/2026
"""
import random
class Coin:
    def __init__(self):
        self.__sideup = 'Heads'
        self.toss()

    def toss(self):

        if random.randint(0, 1)==0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    
    def get_side(self):
        return self.__sideup
