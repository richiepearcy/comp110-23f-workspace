from exercises.ex08.river import River


class my_river:
    day: int
    fish: int
    bears: int

    def __init__(self, fish_init: int, bears_init: int):
        self.fish: int = 10
        self.bears: int = 2
        self.day: int = 0

River.view_river(my_river)
