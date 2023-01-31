import math
import os
from csv import reader

# Random Number Generator Utility Class
class Rand:
    # Random Number Generator Constructor
    def __init__(self, seed = 937162211):
        self.seed = seed

    # Get Next Random Number
    def rand(self, lo = 0, hi = 1):
        self.seed = (16807 * self.seed) % 2147483647
        return lo + (hi - lo) * self.seed / 2147483647

    # Round a number to nPlaces
    @staticmethod
    def rnd(n, nPlaces = 3):
        return round(n, nPlaces)

    # Find Next Integer Random Number
    @staticmethod
    def rint(lo, hi):
        return math.floor(0.5 + Rand.rand(lo, hi))  

# FileWriter Utility Class
class FileWriter:
    # Upload Test Results to a File
    @staticmethod
    def uploadTestResults(items):
        file_path = os.getcwd() + "/etc/out/data.out"
        print(os.getcwd())
        with open(file_path,'w+') as f:
            f.write('\n'.join(items))

# Reader for CSV files
class CSVReader:
    # Read a CSV file
    @staticmethod
    def readCSVFile(fname):
        file_path = os.getcwd() + "/data/" + fname
        col_names= []
        rows = []
        with open(file_path, 'r') as f:
            robj = reader(f, delimiter= ",")
            col_names = []
            rows = []
            # Retrieve the column names
            for row in robj:
                col_names = row
                break
            # Add the rows
            for row in robj:
                rows.append(row)

        return (col_names, rows)



          





    