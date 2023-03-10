# Class for NUM
class NUM:
    # Constructor of NUM
    def __init__(self):
        self.sum = 0
        self.len = 0
        self.mean = 0
        self.moment = 0

    # Add a new number
    def Add(self, num):
        self.len = self.len + 1
        self.sum = self.sum + num
        delta = num - self.mean
        self.mean = self.mean + (delta / self.len)
        self.moment = self.moment + (delta * (num - self.mean))  
    
    # Find mean
    def Mid(self):
        return self.mean
        
    # Find deviation
    def Div(self):
        if(self.moment < 0 or self.len < 2):
            return 0
        else:    
            return pow(self.moment / (self.len - 1), 0.5)