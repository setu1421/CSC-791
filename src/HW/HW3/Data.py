from Utils import *
from Col import *
from Row import *

class DATA:
    def __init__(self, type, filename = None, data = None):
        self.Cols = []
        self.X = []
        self.Y = []
        self.Skip = []
        self.Rows = []
        self.Header = []

        if(type == "file"):
            data = CSVReader.readCSVFile(filename)

        self.CreateCols(data[0])   
        
        for row in data[1]:
            self.Add(row)

    # Create columns
    def CreateCols(self, colNames):
        self.Header = colNames  
        pos = 0
        for name in colNames:
            if name and (name[-1] == '-' or name[-1] == "+" or name[-1] == "!"):
                self.Y.append(pos)
                self.Cols.append(COL(name, pos))
            elif name and (name[-1] == "X"):
                self.Skip.append(pos)
                self.Cols.append(COL(name, pos))    
            elif name:
                self.X.append(pos)
                self.Cols.append(COL(name, pos))

            pos = pos + 1   

    # Add cells
    def Add(self, cells):
        pos = 0
        self.Rows.append(ROW(cells))

        for value in cells:
            if pos not in self.Skip:
                self.Cols[pos].Add(value)
            pos = pos + 1 

    # Clone the data
    def Clone(self, rows = None):
        data = []

        if rows is None:
            for row in self.Rows:
                data.append(row.cells)
        else:
            for row in rows:
                data.append(row.cells)        
        return DATA("clone", None, (self.Header, data))

    # Retrieve status
    def Stats(self, what, cols = None, nPlaces = 2):
        pos = 0
        finalString = what

        for col in self.Cols:
            if (pos not in self.Skip) and (cols and pos in cols):
                if(what == "mid"):
                    mid = str(round(col.num.Mid(), nPlaces)) if col.isNum else str(col.sym.Mid())
                    finalString = finalString + ":" + col.txt + " " + mid + " "
                elif (what == "div"):
                    div = str(round(col.num.Div(), nPlaces)) if col.isNum else str(round(col.sym.Div(), 2))  
                    finalString = finalString + ":" + col.txt + " " + div + " "  
                else:
                    return "Unrecognized stat function"    

            pos = pos + 1

        return finalString            




