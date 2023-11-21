from exercises.ex08.river import River


class my_river:
    fish: int
    bears: int

    def __init__(self, fish_init: int, bears_init: int):
        self.fish: int = 10
        self.bears: int = 2

my_river.view_river()
my_river.one_river_week()
