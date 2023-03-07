from utils import *
from num import NUM
from sym import SYM
from data import Data, sway, stats, div, diffs
from options import options
from num import Num
from sym import Sym
from discretization import *

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


def check_tree():
  data = Data()
  data.read(options['file']) 
  show(data.rows.cluster(), "mid",data.cols.all,1)


def check_sway():
  data = Data()
  data.read(options['file']) 
  best, rest = sway(data)
  print("\nall ", stats(data)[0]) 
  print("    ",   stats(data, div)[0]) 
  print("\nbest", stats(best)[0]) 
  print("    ",   stats(best,div)[0]) 
  print("\nrest", stats(rest)[0]) 
  print("    ",   stats(rest,div)[0]) 
  print("\nall ~= best?", diffs(best["cols"]["y"], data["cols"]["y"]))
  print("best ~= rest?", diffs(best["cols"]["y"], rest["cols"]["y"]))        

def check_bins():
    data = Data()
    data.read(options['file']) 
    best, rest = sway(data)
    print("all","","","",{"best": len(best["rows"]), "rest": len(rest["rows"])})  
    res = bins(data["cols"]["x"], {"best": best["rows"], "rest": rest["rows"]}) 
    for k, t in res.items():
        for _, range in t.items():
            if range["txt"] != b4:
                print("")
            b4 = range["txt"]
            print(range["txt"], range["lo"], range["hi"], rnd(value(range["y"]["has"], len(best["rows"]), len(rest["rows"]), "best")), range["y"]["has"])