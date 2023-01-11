
class Accumulator:
    def __init__(self):
        self._count = 0

    @property  #property decorater   get value not set

    def count(self):
        return self._count 
    
    def add(self, more=1):
        self._count += more 

