"""File to define River class."""
from __future__ import annotations
__author__ = "730318079"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River Ecosystem class set up."""
    # Class Attributes
    day: int
    bears: list
    fish: list
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking Ages of Animals."""
        bear_list: list[Bear] = []
        fish_list: list[Fish] = []
        for x in self.bears:
            if x.age <= 5:
                bear_list.append(Bear())
        for x in self.fish:
            if x.age <= 3:
                fish_list.append(Fish())
        self.bears = bear_list
        self.fish = fish_list
        return None

    def bears_eating(self):
        """Simulating Bears Eating Daily."""
        for x in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                x.eat(3)
        return None
    
    def check_hunger(self):
        """Killing off Bears who haven't eaten."""
        bear_list: list[str] = []
        for x in self.bears:
            if x.hunger_score > 0:
                bear_list.append(Bear())
        self.bears = bear_list
        return None
        
    def repopulate_fish(self):
        """Adding newborn fish."""
        new_fish: int
        new_fish = (len(self.fish) / 2) * 4
        self.fish.append(new_fish)
        return None
    
    def repopulate_bears(self):
        """Adding newborn bears."""
        new_bears: int
        new_bears = (len(self.bears) / 2) * 1
        self.bears.append(new_bears)
        return None
    
    def view_river(self):
        """Viewing current results and stats of river."""
        output: str = f"~~~ Day {self.day}: ~~~\n"
        output += f"Fish population: {self.fish}\n"
        output += f"Bear population: {self.bears}\n"
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for x in self.bears:
            x.one_day()
        # Simulate one day for all Fish
        for x in self.fish:
            x.one_day()
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
        """Simulating one river day into a week."""
        idx: int = 0
        while idx < 7:
            self.one_river_day()
            idx += 1
        return None
    
    def remove_fish(self, amount: int):
        """Removing first in line fish."""
        for x in self.fish:
            self.fish.pop(0)
        return None
