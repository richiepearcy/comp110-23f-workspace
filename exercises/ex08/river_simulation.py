from exercises.ex08.river import River
"""River Simulation."""


class my_river:
    """My Own River Simulation."""
    day: int
    fish: int
    bears: int

    def __init__(self, fish_init: int, bears_init: int):
        """My Constructor."""
        self.fish: int = 10
        self.bears: int = 2
        self.day: int = 0