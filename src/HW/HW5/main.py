#!/usr/bin/env python3

__author__ = "Setu Kumar Basak"
__version__ = "1.0.0"
__license__ = "MIT"


from data import Data
from num import Num
from options import options
from sym import Sym
from utils import *
from TestEngine import *


help = """
main.py : a rep grid processor
(c)2023

USAGE:   main.py  [OPTIONS] [-g ACTION]

OPTIONS:
  -b  --bins    initial number of bins       = 16
  -c  --cliffs  cliff's delta threshold      = .147
  -f  --file    data file                    = ../../etc/data/auto93.csv
  -F  --Far     distance to distant          = .95
  -g  --go      start-up action              = nothing
  -h  --help    show help                    = False
  -H  --Halves  search space for clustering  = 512
  -m  --min     size of smallest cluster     = .5
  -M  --Max     numbers                      = 512
  -p  --p       dist coefficient             = 2
  -r  --rest    how many of rest to sample   = 4
  -R  --Reuse   child splits reuse a parent pole = True
  -s  --seed    random number seed           = 937162211
"""


def main(funs, saved=None, fails=None):
    """
    `main` fills in the settings, updates them from the command line, runs
    the start up actions (and before each run, it resets the random number seed and settongs);
    and, finally, returns the number of test crashed to the operating system.

    :param funs: list of actions to run
    :param saved: dictionary to store options
    :param fails: number of failed functions
    """

    saved, fails = {}, 0
    options.parse_cli_settings(help)

    for k, v in options.items():
        saved[k] = v

    if options['help']:
        print(help)
    else:
        for what, fun in funs.items():
            if options['go'] == "all" or what == options['go']:
                for k, v in saved.items():
                    options[k] = v

                if funs[what]() is False:
                    fails = fails + 1
                    print("❌ fail:", what)
                else:
                    print("✅ pass:", what)
    exit(fails)


# Examples
egs = {}

def eg(key, s, fun):
    global help
    egs[key] = fun
    help += "  -g  {}\t{}\n".format(key, s)

if __name__ == '__main__':    

    eg("the","show options",check_the)
    eg("rand","demo random number generation", check_rand)
    eg("some","demo of reservoir sampling", check_some)
    eg("nums","demo of Num", check_nums)
    eg("syms","demo SYMS", check_syms)
    eg("csv","reading csv files", check_csv)
    eg("data", "showing data sets", check_data)
    eg("clone","replicate structure of a DATA", check_clone)
    eg("cliffs","stats tests", check_cliffs)
    eg("tree","make snd show tree of clusters", check_tree)
    eg("sway","optimizing", check_sway)
    eg("bins","find deltas between best and rest", check_bins)
    main(egs)
