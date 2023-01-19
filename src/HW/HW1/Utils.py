import math

class Rand:
    def __init__(self, seed = 937162211):
        self.seed = seed

    def rand(self, lo = 0, hi = 1):
        self.seed = (16807 * self.seed) % 2147483647
        return lo + (hi - lo) * self.seed / 2147483647

    @staticmethod
    def rnd(n, nPlaces = 3):
        return round(n, nPlaces)
        
    @staticmethod
    def rint(lo, hi):
        return math.floor(0.5 + Rand.rand(lo, hi))    




