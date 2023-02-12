class ex_class:

    def __init__(self, a):
        self.a = a
        
    def ex_fun(self):
        print(__name__)
        print('ex_fun')
        
        return __name__
