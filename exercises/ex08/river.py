"""File to define River class"""
__author__ = "730318079"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:
    day: int
    bears: list
    fish: list
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        bear_list: list[Bear]
        fish_list: list[Fish]
        for x in range(0, len(self.bears)):
            if Bear.age <= 5:
                bear_list.append(Bear())
        for x in range(0, len(self.fish)):
            if Fish.age <= 3:
                fish_list.append(Fish())
        self.bears = bear_list
        self.fish = fish_list
        return None

    def bears_eating(self):
        for x in self.bears:
            if len(self.fish) >= 5:
                River.remove_fish(self, 3)
                Bear.eat(3)
        return None
    
    def check_hunger(self):
        bear_list: list[Bear]
        for x in self.bears:
            if Bear.hunger_score > 0:
                bear_list.append(Bear())
        self.bears = bear_list
        return None
        
    def repopulate_fish(self):
        new_fish: int
        new_fish = (len(self.fish) / 2) * 4
        self.fish.append(new_fish)
        return None
    
    def repopulate_bears(self):
        new_bears: int
        new_bears = (len(self.bears) / 2) * 1
        self.bears.append(new_bears)
        return None
    
    def view_river(self):
        output: str = f"~~~ Day {self.day}: ~~~\n"
        output += f"Fish population: {self.fish}\n"
        output += f"Bear population: {self.bears}\n"
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        factor: int = 7
        self.one_river_day(self * factor)
        return None
    
    def remove_fish(self, amount: int):
        for x in self.fish:
            self.fish.pop(self.fish[0])
        return None
