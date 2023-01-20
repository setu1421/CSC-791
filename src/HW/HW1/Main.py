from CLIParser import *
import sys
from TestEngine import *

if __name__ == "__main__":
    #configs = cli(settings(sys.argv[1:]))
    # Run all test
    ret = runAllTest()   
    # Out exit code from operating system
    sys.exit(ret)