"""File to define Bear class."""


class Bear:
    """Class for Individual Bear."""
    # Bear Attributes
    age: int 
    hunger_score: int
    
    def __init__(self, age_init: int = 0, hunger_init: int = 0):
        """Bear Constructor."""
        self.age = age_init
        self.hunger_score = hunger_init
        return None
    
    def one_day(self):
        """Simulating One Day for Bears."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Factoring Daily Bear Eating."""
        self.hunger_score += num_fish
        return None