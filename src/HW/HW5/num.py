import math
from utils import rnd

# Class for NUM
class NUM:
    # Constructor of NUM
    def __init__(self, at=None, txt=None):
        self.at = at if at else 0
        self.txt = txt if txt else ""
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = float("inf")
        self.hi = float("-inf")
        self.w = -1 if "-" in self.txt else 1
    
    # Add a new number
    def add(self, n):
        if not n =="?":
            self.n += 1
            d = n - self.mu
            self.mu = self.mu + d / self.n
            self.m2 = self.m2 + d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)
    
    # Find mean
    def mid(self):
        return self.mu
    
    # Find deviation
    def div(self):
        if (self.m2 < 0 or self.n < 2):
            return 0
        else:
            return math.pow((self.m2 / (self.n - 1)),0.5)
        
    # Round numbers to n decimal points
    def rnd(self,x,n):
        if x == "?":
            return x
        else:
            return rnd(x,n)
    
    # Normalize the number
    def norm(self, n):
        return n if n == "?" else (n - self.lo)/(self.hi - self.lo + 1E-32)
    
    # Calculate the distance between two numbers
    def dist(self, n1, n2):
        if n1=="?" and n2=="?":
            return 1
        n1,n2 = self.norm(n1), self.norm(n2)
        if n1=="?": 
            n1 = 1 if n2<.5 else 0
        if n2=="?":
            n2 =  1 if n1<.5 else 0
        return abs(n1 - n2)