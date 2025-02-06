#!/usr/bin/python3
"""
Module to create an abstract class named Animal using the ABC package.
This class should have an abstract method called sound.
Create two subclasses of Animal: Dog and Cat.
Implement the sound method in each subclass
to return the strings “Bark” and “Meow” respectively.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class named Animal using the ABC package.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Subclass of the Animal class.
    """

    def sound(self):
        """
        Implement the sound method to return the string “Bark”.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass of the Animal class.
    """

    def sound(self):
        """
        Implement the sound method to return the string “Meow”.
        """
        return "Meow"
