from Num import NUM
from Sym import SYM
from Utils import *
from Config import *
from Data import *

# Test case of sym
def test_sym():
    sym = SYM()
    input = ["a", "a", "a", "a", "b", "b", "c"]
    for val in input:
        sym.Add(val)
    return ((sym.Mid() == "a") and (sym.Div() - 1.379) < 0.01)

# Test case for num
def test_num():
    num = NUM()
    input = [1,1,1,1,2,2,3]
    for val in input:
        num.Add(val)   
    return ((num.Mid() - 1.5714285714285714) < 0.01 and (num.Div() - 0.787) < 0.01)

# Test case for rand
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

# Test case for the
def test_the():
    return True if len(config) > 0 else False

# Test case for csv
def test_csv():
    ret = CSVReader.readCSVFile("auto93.csv")
    col_len = len(ret[0])
    row_len = len(ret[1])
    return col_len*row_len == 8*398

# Test case for data
def test_data():
    data = DATA("file", "auto93.csv")

    return (len(data.Rows) == 398 and data.Cols[data.Y[0]].num.weight == -1.0
    and data.Cols[data.X[1]].at == 1 and len(data.X) == 4)

# Test case for stats
def test_stats():
    data = DATA("file", "auto93.csv")
    data.Stats("mid", data.X, 2)
    data.Stats("div", None, 2)

    return True

# Test case for clone
def test_clone():
    data1 = DATA("file", config["file"])   
    data2 = data1.Clone()
    result = (len(data1.Rows) == len(data2.Rows) and 
    data1.X[0] == data2.X[0] and len(data1.X) == len(data2.X))

    return result 

# Test case for around
def test_around():
    data = DATA("file", config["file"]) 
    vals = data.around(data.Rows[0], data.Rows)
    
    for ind,val in enumerate(vals):
        if (ind % 50) == 0:
            print(val)

    return True  

# Test case for half
def test_half():
    data = DATA("file", config["file"]) 
    res = data.Half()

    return True

# Test case for cluster
def test_cluster():
    data = DATA("file", config["file"]) 
    node = data.Cluster()

    return True 

# Test case for cluster
def test_sway():
    data = DATA("file", config["file"]) 
    node = data.Sway()

    return True         

     

# Run all test cases and return
def runAllTest(configs = None):
    fails = 0
    list = []
    # Test 1
    test_status = test_sym()
    if test_status == False: 
        fails = fails + 1
        list.append("❌ fail:  sym") 
    else:
       list.append("✅ pass:  sym")  
    # Test 2
    test_status = test_num()
    if test_status == False: 
        fails = fails + 1
        list.append("❌ fail:  num") 
    else:
        list.append("✅ pass:  num")

    # Test 3
    test_status = test_rand()
    if test_status == False:
        fails = fails + 1 
        list.append("❌ fail:  rand") 
    else:
        list.append("✅ pass:  rand")


    # Test 4
    test_status = test_the()
    if test_status == False:
        fails = fails + 1
        list.append("❌ fail:  the")     
    else:
        list.append("✅ pass:  the")

    # Test 5
    test_status = test_csv()
    if test_status == False:
        fails = fails + 1
        list.append("❌ fail:  csv")     
    else:
        list.append("✅ pass:  csv")   

    # Test 6
    test_status = test_data()
    if test_status == False:
        fails = fails + 1
        list.append("❌ fail:  data")     
    else:
        list.append("✅ pass:  data")  
    
    # Test 7
    test_status = test_stats()
    if test_status == False:
        fails = fails + 1
        list.append("❌ fail:  stats")     
    else:
        list.append("✅ pass:  stats")   

    # Test 8
    test_status = test_clone()
    if test_status == False:
        fails = fails + 1
        list.append("❌ fail:  clone")     
    else:
        list.append("✅ pass:  clone") 

    # Test 9
    test_status = test_around()
    if test_status == False:
        fails = fails + 1
        list.append("❌ fail:  around")     
    else:
        list.append("✅ pass:  around")  

    # Test 10
    test_status = test_half()
    if test_status == False:
        fails = fails + 1
        list.append("❌ fail:  half")     
    else:
        list.append("✅ pass:  half") 

    # Test 11
    test_status = test_cluster()
    if test_status == False:
        fails = fails + 1
        list.append("❌ fail:  cluster")     
    else:
        list.append("✅ pass:  cluster")   

    # Test 12
    test_status = test_sway()
    if test_status == False:
        fails = fails + 1
        list.append("❌ fail:  sway")     
    else:
        list.append("✅ pass:  sway")                
    
    # Upload the test results 
    FileWriter.uploadTestResults(list)    

    return fails     