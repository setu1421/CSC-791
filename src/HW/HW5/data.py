from row import ROW
from cols import COLS
from utils import *
from operator import itemgetter

# Class for DATA
class DATA:
    # Constructor of DATA
    def __init__(self, src):
        self.rows = []
        self.cols = None
        # Check if a file type and read for source file else read from list
        if isinstance(src, str):
            csv(src, self.add)
        else:
            for row in src:
                self.add(row)

    # Add the data
    def add(self, t):
        if self.cols:
            t = ROW(t) if type(t) == list else t
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols=COLS(t)

    # Stats of data
    def stats(self, what, cols, nPlaces):
        # Return stat based on div or mid
        def fun(_, col):
            if what == 'div':
                val = col.div()
            else:
                val = col.mid()
            return col.rnd(val, nPlaces),col.txt
        return kap(cols or self.cols.y, fun)
    
    # Calculate Distance 
    def dist(self, row1, row2, cols = None):
        n,d = 0,0
        for col in cols or self.cols.x:
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at])**the['p']
        return (d/n)**(1/the['p'])
    
    # Clone the data
    def clone(self, init = {}):
        data = DATA([self.cols.names])
        _ = list(map(data.add, init))
        return data
    
    # Sort other rows based on row1 
    def around(self, row1, rows = None, cols = None):
        def function(row2):
            return {'row' : row2, 'dist' : self.dist(row1,row2,cols)} 
        return sorted(list(map(function, rows or self.rows)), key=itemgetter('dist'))
    
    # Find furthest point
    def furthest(self, row1, rows = None, cols = None):
        t=self.around(row1,rows,cols)
        return t[len(t) - 1]

    # Retrieve best half recursively
    def sway(self, rows=None, min=None, cols=None, above=None):
        rows = rows or self.rows
        min = min or len(rows) ** the['min']
        cols = cols or self.cols.x
        node = {'data': self.clone(rows)}
        if len(rows) > 2 * min:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows, cols, above)
            if self.better(node['B'], node['A']):
                left, right, node['A'], node['B'] = right, left, node['B'], node['A']
            node['left'] = self.sway(left, min, cols, node['A'])
        return node
    
    # Find if Row1 dominates Row2
    def better(self, row1, row2):
        s1, s2, ys = 0, 0, self.cols.y
        for col in ys:
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x - y) / len(ys))
            s2 = s2 - math.exp(col.w * (y - x) / len(ys))
        return s1 / len(ys) < s2 / len(ys)
    
    # Divide data using two far points
    def half(self, rows = None, cols = None, above = None):
        def dist(row1,row2): 
            return self.dist(row1,row2,cols)
        rows = rows or self.rows
        A    = above or any(rows)
        B    = self.furthest(A,rows)['row']
        c    = dist(A,B)
        left, right = [], []
        def project(row):
            x, y = cosine(dist(row,A), dist(row,B), c)
            try:
                row.x = row.x
                row.y = row.y
            except:
                row.x = x
                row.y = y
            return {'row' : row, 'x' : x, 'y' : y}
        for n,tmp in enumerate(sorted(list(map(project, rows)), key=itemgetter('x'))):
            if n < len(rows)//2:
                left.append(tmp['row'])
                mid = tmp['row']
            else:
                right.append(tmp['row'])
        return left, right, A, B, mid, c
    
    # Recursively cluster the rows
    def cluster(self, rows = None , cols = None, above = None):
        rows = rows or self.rows
        cols = cols or self.cols.x
        node = { 'data' : self.clone(rows) }
        if len(rows) >= 2:
            left, right, node['A'], node['B'], node['mid'], node['c'] = self.half(rows,cols,above)
            node['left']  = self.cluster(left,  cols, node['A'])
            node['right'] = self.cluster(right, cols, node['B'])
        return node