from TestEngine import TestEngine
import sys

if __name__ == "__main__":    
    test_list1 = [1, 1, 1, 1, 2, 2, 3]
    print(TestEngine.RunTest(test_list1, "num"))
    test_list2 = ["a", "a", "a", "a", "b", "b", "c"] 
    print(TestEngine.RunTest(test_list2, "sym"))
    
    sys.exit(1)