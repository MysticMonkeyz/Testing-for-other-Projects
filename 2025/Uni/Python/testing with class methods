class parent:
    
    def __init__(self, bar):
        self.bar = bar
        
    def fun(self):
        
        print(self.bar)
        
    def take1(self):
        self.bar -= 1.0
        self.bar = round(self.bar, 2)
    
class son(parent):
    
    def __init__(self):
        super().__init__(bar = 3.14)

class daughter(parent):

    def __init__(self):
        super().__init__(bar = 2.74)
    
son1 = son()
daughter1=daughter()
son2 = son()

son1.fun()
son1.take1()
son1.fun()
daughter1.fun()
daughter1.take1()
daughter1.fun()

son2.fun()
