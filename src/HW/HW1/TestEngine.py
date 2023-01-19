from NUM import NUM
from SYM import SYM
from Utils import Rand

class TestEngine:
    @staticmethod
    def RunTest(input, test_no):
        if(test_no == "test1"):
            num = NUM()
            for val in input:
                num.Add(val)   
            return ((num.Mid() - 1.5714285714285714) < 0.01 and (num.Div() - 0.787) < 0.01)
        elif(test_no == "test2"):
            sym = SYM()
            for val in input:
                sym.Add(val)
            return ((sym.Mid() == "a") and (sym.Div() - 1.379) < 0.01)
        elif(test_no == "test3"):
            num1 = NUM()
            num2 = NUM()
            rand1 = Rand()
            for i in range(1, 1000):
                num1.Add(rand1.rand(0,1)) 
            rand2 = Rand()
            for i in range(1, 1000):
                num2.Add(rand2.rand(0,1))     
            m1 = Rand.rnd(num1.Div(), 10)
            m2 = Rand.rnd(num2.Div(), 10)        

            return (m1 == m2) and (0.5 == Rand.rand(m1, 1))


