import math

# Class for NUM
class NUM:
    # Constructor of NUM
    def __init__(self):
        self.sum = 0
        self.len = 0
        self.mean = 0
        self.moment = 0
        self.weight = 1
        self.low = float('inf')
        self.high = float('-inf')

    # Add a new number
    def Add(self, num):
        self.len = self.len + 1
        self.sum = self.sum + num
        delta = num - self.mean
        self.mean = self.mean + (delta / self.len)
        self.moment = self.moment + (delta * (num - self.mean))  
        self.high = max(self.high, num)
        self.low = min(self.low, num)
    
    # Find mean
    def Mid(self):
        return self.mean
        
    # Find deviation
    def Div(self):
        if(self.moment < 0 or self.len < 2):
            return 0
        else:    
            return pow(self.moment / (self.len - 1), 0.5)

    # Round numbers to n decimal points
    def Round(self, x, n):
        if x == "?":
            return x
        else:
            return round(x, n) 

    # Normalize the number
    def Norm(self, n): 
        if n == "?": 
            return n 
        else: 
            n = float(n)
            return (n - self.low) / (self.high - self.low + (10**-32))   
    
    # Calculate the distance between two numbers
    def Distance(self, n1, n2): 
        if n1 == "?" and n2 == "?": 
            return 1
        else: 
            n1 = self.Norm(n1)
            n2 = self.Norm(n2)
            # AHA's assumption
            if n1 == "?" and n2 < .5: 
                n1 = 1
            else: 
                n1 = 0
            if n2 == "?" and n1 < .5: 
                n2 = 1
            else: 
                n2 = 0 
            
            return abs(n1 - n2)                     