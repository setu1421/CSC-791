from copy import deepcopy
from Data import *
import io
import json
import math
import random
import re

class Grid:
    @staticmethod
    def transpose(t):
        u = []
        for i in range(0, len(t[1])):
            u.append([])
            for j in range(0, len(t)):
                u[i].append(t[j][i])
        return u 
    
    @staticmethod
    def repCols(cols):
        cols = deepcopy(cols)
        print(cols)
        for _,col in enumerate(cols):
            col[len(col) - 1] = col[0] + ":" + col[len(col) - 1]
            for j in range(1, len(col)):
                col[j - 1] = col[j]
            col.pop()
        first_col = ['Num' + str(k+1) for k in range(len(cols[1])-1)]
        first_col.append('thingX')
        cols.insert(0, first_col)
        return DATA("cols", None, cols)
    
    @staticmethod
    def repRows(t, rows):
        rows = deepcopy(rows)
        for j,s in enumerate(rows[-1]):
            rows[0][j] = str(rows[0][j]) + ":" + s
        rows.pop()
        for n, row in enumerate(rows):
            if n==0:
                row.append("thingX")
            else:
                u = t['rows'][- n]
                row.append(u[len(u) - 1])
        return DATA("rows", None, rows)

    
    @staticmethod
    def dofile(sFile):
        with open(sFile, 'r', encoding = 'utf-8') as f:
            text  = re.findall(r'(?<=return )[^.]*', f.read())[0].replace('{', '[').replace('}',']').replace('=',':').replace('[\n','{\n' ).replace(' ]',' }' ).replace('\'', '"').replace('_', '"_"')
            return json.loads(re.sub("(\w+):", r'"\1":', text))