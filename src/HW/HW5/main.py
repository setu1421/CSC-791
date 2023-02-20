#!/usr/bin/env python3

__author__ = "Setu Kumar Basak"
__version__ = "1.0.0"
__license__ = "MIT"


from data import Data
from num import Num
from options import options
from sym import Sym
from utils import csv, rnd, rand, set_seed, oo, rint, adds, cliffsDelta

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

def check_the():
    return str(options)

def check_rand():
    set_seed(1)
    t = []
    for i in range(1, 1000 + 1):
        t.append(rint(100))

    set_seed(1)
    u = []
    for i in range(1, 1000 + 1):
        u.append(rint(100))

    for k, v in enumerate(t):
        assert v == u[k]
        

def check_some():
    options['Max'] = 32
    num1 = Num()
    for i in range(1,10000+1):
        num1.add(i)
    print(num1.has())

def check_nums():
    num1,num2 = Num(), Num()
    
    set_seed(options["seed"])
    for i in range(1, 10000 + 1):
        num1.add(rand())

    for i in range(1, 10000 + 1):
        num2.add(rand()**2)
    print(1,rnd(num1.mid()), rnd(num1.div()))
    print(2,rnd(num2.mid()), rnd(num2.div())) 
    return .5 == rnd(num1.mid()) and num1.mid()> num2.mid()

def check_syms():
    sym=Sym()
    adds(sym, ["a","a","a","a","b","b","c"])
    print (sym.mid(), rnd(sym.div())) 
    return 1.38 == rnd(sym.div())

def check_csv():
    n=0
    def f(t):
        nonlocal n
        n += len(t)
    csv(options['file'], f) 
    return 3192 == n

def check_data():
    data=Data()
    data.read(options['file'])
    col=data.cols.x[0]
    print(col.lo,col.hi, col.mid(),col.div())
    oo(data.stats())

def check_clone():
    data1=Data()
    data1.read(options['file'])
    data2=Data()
    data2.clone(data1,data1.rows) 
    oo(data1.stats())
    oo(data2.stats())

def check_cliffs():
    assert(False == cliffsDelta( [8,7,6,2,5,8,7,3],[8,7,6,2,5,8,7,3]),"1")
    assert(True  == cliffsDelta( [8,7,6,2,5,8,7,3], [9,9,7,8,10,9,6]),"2") 
    t1,t2=[],[]
    for i in range(1,1000+1):
        t1.append(rand()) 
    for i in range(1,1000+1):
        t2.append(rand()**.5)
    assert(False == cliffsDelta(t1,t1),"3") 
    assert(True  == cliffsDelta(t1,t2),"4") 
    diff,j=False,1.0
    while not diff:
        def f(x):
            nonlocal j
            return x*j
        t3=map(f, t1)
        diff=cliffsDelta(t1,t3)
        print(">",rnd(j),diff) 
        j=j*1.025

eg("the","show options",check_the)

eg("rand","demo random number generation", check_rand)

eg("some","demo of reservoir sampling", check_some)

# eg("nums","demo of Num", check_nums)

eg("syms","demo SYMS", check_syms)

eg("csv","reading csv files", check_csv)

# eg("data", "showing data sets", check_data)

# eg("clone","replicate structure of a DATA", check_clone)

eg("cliffs","stats tests", check_cliffs)
  

main(egs)
