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
    def Round(x, n):
        if x == "?":
            return x
        else:
            return round(x, n)        