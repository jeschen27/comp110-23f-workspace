"""Practice with classes and methods!"""

from __future__ import annotations

__author__ = "730658911"


class Point:
    """Creates a class with two attributes, x and y, of type float."""
    x: float
    y: float
    
    def __init__(self, x_init: float, y_init: float):
        """My Constructor. Defines what happens when a new object of class Point is created."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates the attributes to increase by a give input factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Creates a new object of class Point with the attributes that have been increased by a given factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point