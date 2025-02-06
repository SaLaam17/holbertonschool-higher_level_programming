#!/usr/bin/env python3
"""
Module that defines a FlyingFish class
that inherits from both
a Fish class and a Bird class.
"""


class Fish:
    """
    class with methods swim and habitat.
    """

    def swim(self):
        """
        Method that prints "The fish is swimming"
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Method that prints "The fish lives in water"
        """
        print("The fish lives in water")


class Bird:
    """
    class with methods fly and habitat.
    """

    def fly(self):
        """
        Method that prints "The bird is flying""
        """
        print("The bird is flying")

    def habitat(self):
        """
        Method that prints "The bird lives in the sky"
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class that inherits from both Fish and Bird.
    """

    def fly(self):
        """
        Method that override the fly method.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Method that override the swim method.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Method that override the habitat method.
        """
        print("The flying fish lives both in water and the sky!")
