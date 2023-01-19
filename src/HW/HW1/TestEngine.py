from NUM import NUM
from SYM import SYM
from Utils import Rand
from Config import *

def test_sym():
    sym = SYM()
    input = ["a", "a", "a", "a", "b", "b", "c"]
    for val in input:
        sym.Add(val)
    return ((sym.Mid() == "a") and (sym.Div() - 1.379) < 0.01)


def test_num():
    num = NUM()
    input = [1,1,1,1,2,2,3]
    for val in input:
        num.Add(val)   
    return ((num.Mid() - 1.5714285714285714) < 0.01 and (num.Div() - 0.787) < 0.01)

def test_rand():
    num1 = NUM()
    num2 = NUM()
    seed = 937162211
    rand1 = Rand(seed)
    for i in range(1, 1001):
        num1.Add(rand1.rand(0,1)) 
    rand2 = Rand(seed)
    for i in range(1, 1001):
        num2.Add(rand2.rand(0,1))     
    m1 = Rand.rnd(num1.Div(), 10)
    m2 = Rand.rnd(num2.Div(), 10)       

    return (m1 == m2) and (0.3 == Rand.rnd(m1, 1))

def test_the():
    return True if len(config) > 0 else False


def runAllTest():
    fails = 0
    # Test 1
    test_status = test_sym()
    if test_status == False: 
        fails = fails + 1
    # Test 2
    test_status = test_num()
    if test_status == False: 
        fails = fails + 1
    # Test 3
    test_status = test_rand()
    if test_status == False:
        fails = fails + 1 

    # Test 4
    test_status = test_the()
    if test_status == False:
        fails = fails + 1    

    return fails     