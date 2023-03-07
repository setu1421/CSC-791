import math
from sym import SYM
from num import NUM

# Class for COLS
class COLS:
    # Constructor function
    def __init__(self, t):
        self.names = t
        self.all = []
        self.x = []
        self.y = []
        self.klass = None
        # Add each column into all based on numeric or symbolic
        for col_name in t:
            if col_name[0].isupper():
                col = NUM(t.index(col_name), col_name)
            else:
                col = SYM(t.index(col_name), col_name)
            self.all.append(col)
            # Retrieve Y and X columns
            if not col_name[-1] == "X":
                if "+" in col_name or "!" in col_name:
                    self.y.append(col)
                else:
                    self.x.append(col)
                if "!" in col_name:
                    self.klass=col

    # Add rows to each columns  
    def add(self, row):
        for t in [self.x, self.y]:
            for col in t:
                col.add(row.cells[col.at])