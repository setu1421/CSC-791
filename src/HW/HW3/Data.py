from Utils import *
from Col import *
from Row import *
import math
from Config import *

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
    
    # Find if Row1 dominates Row2
    def Better(self, row1, row2):
        s1 = 0.0
        s2 = 0.0

        for pos in self.Y:
            res1 = self.Cols[pos].Norm(str(row1.cells[pos]))
            x = res1[1] if res1[0] == True else res1[1]
            w = self.Cols[pos].num.weight if self.Cols[pos].isNum else 1
            res2 = self.Cols[pos].Norm(str(row2.cells[pos]))
            y = res2[1] if res2[0] == True else res2[1]
            s1 = s1 - math.exp(w * (x - y) / len(self.Y))
            s2 = s2 - math.exp(w * (y - x) / len(self.Y))

        return ((s1 / len(self.Y)) < (s1 / len(self.Y))) 
    
    # Calculate distance between row1 and row2
    def Distance(self, row1, row2):
        n = 0
        d = 0.0

        for pos in self.X:
            n = n + 1
            d = d + self.Cols[pos].Distance(str(row1.cells[pos]), str(row2.cells[pos]))

        return math.pow((d/n), (1 / config["distcoeff"]))    
    
    # Sort other rows based on row1 
    def around(self, row1, rows):
        rows = rows if rows else self.Rows
        def func(row2):
            return {'row': row2, 'dist': self.Distance(row1, row2)}
        
        return sorted(list(map(func, rows)), key = lambda k: k['dist'])
    
    # Divide data using two far points
    def Half(self, rows = None, above = None):
        rows = rows if rows else self.Rows
        some = Utils.Many(rows, config["sample"])  
        A = above if above else Utils.Any(rows)[0]
        B = self.around(A, some)[int((config["faraway"]  * len(rows)) // 1)]["row"]
        C = self.Distance(A, B)

        left, right, projections = [], [], []

        for row in rows:
            distances = Utils.Cosine(self.Distance(row, A), self.Distance(row, B), C)
            projections.append((row, distances[0], distances[1]))

        sorted_projections = sorted(projections, key= lambda x: x[2])

        n = 0
        half = int(len(rows)/ 2)    
        mid = None

        for proj in sorted_projections:
            if(n <= half):
                left.append(proj[0])
                mid = proj[0]
            else:
                right.append(proj[0]) 
                
            n = n + 1  

        return (left, right, A, B, mid, C)    

    # Recursively cluster the rows
    def Cluster(self, rows = None, min =  float('inf'), above = None):
        rows = rows if rows else self.Rows
        min = min if (min == float('inf')) else math.pow(len(rows), config["minstopclusters"])
        node = {"data": self.Clone(rows)}

        if(len(rows) > 2 * min):
            left, right, A, B = self.Half(rows, above)
            node.left = self.Cluster(left, min, A)
            node.right = self.Cluster(right, min, B)

        return node 

    # Return best half recursively
    def Sway(self, rows = None, min =  float('inf'), above = None):   
        rows = rows if rows else self.Rows
        min = min if (min == float('inf')) else math.pow(len(rows), config["minstopclusters"])
        node = {"data": self.Clone(rows)}

        if(len(rows) > 2 * min):
            left, right, A, B = self.Half(rows, above)
            if self.Better(A, B):
                left, right, A, B = right, left, B, A
            node['left'] = self.Sway(left, min, A)
        return node 

    # prints the tree generated from `DATA:tree`
    def show(self, node, what, cols, nPlaces, lvl): 
        if node: 
            if lvl is None:
                lvl = 0
            for i in range(0, lvl): 
                print("| ", end = "")
            print(len(self.rows), end = "  ")

            if not node.left or lvl == 0: 
                print(self.Stats("mid", node["data"].Y, nPlaces))
            
            # recursive call 
            self.show(node.left, what, cols, nPlaces, lvl+1)
            self.show(node.right, what, cols, nPlaces, lvl+1)           






           



    

    



