from NUM import NUM
from SYM import SYM

class TestEngine:
    @staticmethod
    def RunTest(input, type):
        if(type == "num"):
            num = NUM()
            for val in input:
                num.Add(val)   
            return ((num.Mid() - 1.5714285714285714) < 0.01 and (num.Div() - 0.787) < 0.01)
        elif(type == "sym"):
            sym = SYM()
            for val in input:
                sym.Add(val)
            return ((sym.Mid() == "a") and (sym.Div() - 1.379) < 0.01)  


