"""CQ07!"""
from __future__ import annotations
__author__ = "730318079"


class Point:
    # attributes
    """class definition."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor."""
        self.x = x_init
        self.y = y_init
        # returns a point 

    def scale_by(self, factor: int) -> None:
        """Mutates point."""
        self.x = self.x * factor
        self.y = self.y * factor
        # returns a new point with new x and y values

    def scale(self, factor: int) -> Point:
        """Mutates point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    # returns a new point mutated by factor

    def __str__(self) -> str:
        """Magic Method to reroute str."""
        point_info: str = f"x: {self.x}; y: {self.y}"
        return point_info
    # returns x and y values in correct str notation
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplication operator overload."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    # returns x and y multiplied by factor 

    def __add__(self, factor: int | float) -> Point:
        """Addition operator overload."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point
    # returns x and y added by the factor