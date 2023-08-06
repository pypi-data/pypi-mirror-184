from fns import math_funcs as mf

class Grotot:
    def __init__(self, age:int = 0) -> None:
        self.age = age
    
    def incrementAge(self):
        self.age = mf.squareAdd(self.age, 1)