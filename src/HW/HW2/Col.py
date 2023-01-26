from Num import *
from Sym import *

# Definition for one column
class COL:
    def __init__(self, name, pos):
        self.txt = name
        self.at = pos

        self.Parse(name)
    
    # Parse the column information
    def Parse(self, name):
        if name and name[0].isupper():
            self.isNum = True
            self.N = 0
            self.num = NUM()
            self.num.weight = -1.0 if name[-1] == '-' else 1.0
        elif name and (not name[0].isupper()):
            self.isNum = False
            self.N = 0
            self.sym = SYM()  
        else:
            raise Exception("Column Name Error.")   

    # Add values to column 
    def Add(self, value):
        if(value != "?"):
            self.N = self.N + 1
            if(self.isNum):
                self.num.Add(float(value))
            else:
                self.sym.Add(value)            


