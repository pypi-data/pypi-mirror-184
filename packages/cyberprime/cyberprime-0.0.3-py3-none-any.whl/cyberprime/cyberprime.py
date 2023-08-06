from .utils.math_funs import *

def short(x):
    return funcAdd(x, x)

class A:
    """
    Temprory class A
    """
    def __init__(self, xval:float, yval:float) -> None:
        self.xval = xval
        self.yval = yval
        pass
    
    def printMe(self):
        print(f"xval: {self.xval} + yval: {self.yval}")

class B:
    """
    Temprory class B
    """
    def __init__(self, xvalu:float, yvalu:float) -> None:
        self.xvalu = xvalu
        self.yvalu = yvalu
        pass
    
    def printMe(self):
        print(f"xval: {self.xvalu} + yval: {self.yvalu}")