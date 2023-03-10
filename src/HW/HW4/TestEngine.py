from utils import *
from num import NUM
from sym import SYM
from data import DATA

# Test case for the
def test_the():
    print(the.__repr__())

# Test case for copy
def test_copy():
  t1 = {'a' : 1, 'b' : { 'c' : 2, 'd' : [3]}}
  t2 = deepcopy(t1)
  t2['b']['d'][0] = 10000
  print('b4', t1, '\nafter', t2)

# Test case for sym
def test_sym():
    sym = SYM()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == rnd(sym.div())

# Test case for num
def test_num():
    num = NUM()
    for x in [1,1,1,1,2,2,3]:
        num.add(x)
    return 11/7 == num.mid() and 0.787 == rnd(num.div())

# Test case for repcols
def test_repCols():
    t = repCols(dofile(the['file'])['cols'], DATA)
    _ = list(map(oo, t.cols.all))
    _ = list(map(oo, t.rows))

# Test case for synonyms
def test_synonyms():
    data = DATA(the['file'])
    show(repCols(dofile(the['file'])['cols'], DATA).cluster(),"mid",data.cols.all,1)

# Test case for reprows
def test_repRows():
    t=dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    _ = list(map(oo, rows.cols.all))
    _ = list(map(oo, rows.rows))

# Test case for prototypes
def test_prototypes():
    t = dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    show(rows.cluster(),"mid",rows.cols.all,1)

# Test case for position
def test_position():
    t = dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    rows.cluster()
    repPlace(rows)

# Test case for every
def test_every():
    repgrid(the['file'], DATA)