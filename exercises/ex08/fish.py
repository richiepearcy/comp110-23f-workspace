"""File to define Fish class."""

class Fish:
    """Class for individual Fish."""
    age: int
    
    def __init__(self, age_init: int = 0):
        """Fish Constructor."""
        self.age = age_init
        return None
    
    def one_day(self):
        """Aging Individual Fish's by 1."""
        self.age += 1
        return None