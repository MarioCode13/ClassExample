from abc import abstractmethod,ABC
class TouchScreenLaptop(ABC):
    def __init__(self,make,model):
        self.make=make
        self.model=model
        
    @abstractmethod
    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass
    
    
class HP(TouchScreenLaptop):
    def __init__(self,make,model):
        TouchScreenLaptop.__init__(self,make,model)       
    def scroll(self):
        print('scrolling')
    
        
class DELL(TouchScreenLaptop):
    def __init__(self,make,model):
        TouchScreenLaptop.__init__(self,make,model)        
    def scroll(self):
        print('scrolling')


class HPNotebook(HP):
    def __init__(self,touchSensor,make,model):
        super().__init__(make, model)
        self.touchSensor=touchSensor        
    def scroll(self):
        print('smooth scrolling')
    def click(self):
        print('clicked')
        
class DellNotebook(DELL):
    def __init__(self,make,model):
        super().__init__(make, model)    
    def scroll(self):
        print('smooth scrolling')
    def click(self):
        print('clicked')
        
        
myHP= HPNotebook(True,'Note2', 'H200')
print(myHP.make)

myDell=DellNotebook('ZenBook','D200')
print(myDell.model)

myHP.click()
myDell.click()
myHP.scroll()
myDell.scroll()