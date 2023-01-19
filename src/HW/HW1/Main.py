from CLIParser import *
import sys
from TestEngine import *

if __name__ == "__main__":
    #configs = cli(settings(sys.argv[1:]))
    ret = runAllTest()   
    sys.exit(ret)