from TestEngine import TestEngine
import sys

if __name__ == "__main__":    
    fails = 0
    # Test 1
    test_list1 = [1, 1, 1, 1, 2, 2, 3]
    test_status = TestEngine.RunTest(test_list1, "test1")
    if test_status: 
        fails = fails + 1
    # Test 2
    test_list2 = ["a", "a", "a", "a", "b", "b", "c"] 
    if TestEngine.RunTest(test_list2, "test2") == False: 
        fails = fails + 1
    # Test 3
    test_seed = 937162211
    if TestEngine.RunTest(test_seed, "test3") == False:
        fails = fails + 1    

    
    sys.exit(fails)