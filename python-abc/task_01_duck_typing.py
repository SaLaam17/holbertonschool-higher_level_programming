#!/usr/bin/python3
"""
Module that:
- defines abstract class named Shape
with two abstract methods: area and perimeter.
- Two classes Circle and Rectangle, both inheriting from Shape.
Each class should provide implementations for the area and perimeter methods.
"""
from abc import ABC, abstractmethod
import math

def shape_info(shape):
        """
        Standalone function that accepts an object of type Shape.
        """
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")

class Shape(ABC):
    """
    Abstract class named Shape using the ABC package.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter
        """
        pass


class Circle(Shape):
    """
    Class that inherit from Shape class.
    """

    def __init__(self, radius):
        """
        Initialize
        """
        self.radius = radius

    def area(self):
        """
        Abstract method to calculate the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the circle.
        """
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Class that inherit from Shape class.
    """

    def __init__(self, width, height):
        """
        Initialize
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Abstract method to calculate the area of the rectangle.
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the rectangle.
        """
        return (self.width + self.height) * 2
