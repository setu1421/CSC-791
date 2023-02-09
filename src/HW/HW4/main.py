#!/usr/bin/env python3

__author__ = "Setu Kumar Basak"
__version__ = "1.0.0"
__license__ = "MIT"

from utils import *
from TestEngine import *

def main():
    saved,fails={},0
    list = []
    # Read the CLI settings
    for k,v in cli(settings(help)).items():
        the[k] = v
        saved[k] = v
    # Print help if "help" is passed    
    if the['help'] == True:
        print(help)
    else:
        # Run for each test cases
        for what, fun in egs.items():
            if the['go'] == 'all' or the['go'] == what:
                for k,v in saved.items():
                    the[k] = v
                Seed = the['seed']
                if egs[what]() == False:
                    fails += 1
                    list.append('❌ fail: ' + what)
                else:
                    list.append('✅ pass: ' + what)
    # Upload the test results             
    FileWriter.uploadTestResults(list, "grid") 
    # Return the fails if any               
    sys.exit(fails)

if __name__ == '__main__':
    # Test Cases
    eg('the', 'show settings', test_the)
    eg('copy','check copy', test_copy)
    eg('sym', 'check syms', test_sym)
    eg('num', 'check nums', test_num)
    eg('repcols', 'checking repcols', test_repCols)
    eg('synonyms','checking repcols cluster', test_synonyms)
    eg('reprows','checking reprows', test_repRows)
    eg('prototypes','checking reprows cluster', test_prototypes)
    eg('position','where\'s wally', test_position)
    eg('every','the whole enchilada', test_every)
    # Call the main function
    main()