from TestEngine import TestEngine
import sys

if __name__ == "__main__":    
    fails = 0
    test_list1 = [1, 1, 1, 1, 2, 2, 3]
    if TestEngine.RunTest(test_list1, "num") == False: fails = fails + 1
    test_list2 = ["a", "a", "a", "a", "b", "b", "c"] 
    if TestEngine.RunTest(test_list2, "sym") == False: fails = fails + 1
    
    sys.exit(fails)