"""File to define Fish class"""

class Fish:
    age: int
    
    def __init__(self, age_init: int = 0):
        self.age = age_init
        return None
    
    def one_day(self):
        self.age += 1
        return None