import math

# Class for SYM
class SYM:
    # Constructor of SYM
    def __init__(self):
        self.count = 0
        self.len = 0
        self.entropy = 0
        self.most = 0
        self.mode = ""
        self.has = {}
    # Add a new string
    def Add(self, x):
        if(self.has.get(x)):
            self.has[x] = self.has[x] + 1
        else:
            self.count = self.count + 1
            self.has[x] = 1

        self.len = self.len + 1

        if(self.has[x] > self.most):
            self.most = self.has[x]
            self.mode = x    
    # Find the mode of string
    def Mid(self):
        return self.mode
    # Find the entropy of string
    def Div(self):
        if(self.len <= 0): 
            return 0

        probs = []
        for value in self.has.values():
            probs.append((value / self.len))

        for prob in probs:
            self.entropy = self.entropy - (prob * math.log2(prob)) 

        return self.entropy       



