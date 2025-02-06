#!/usr/bin/env python3
"""
Module to define two mixin classes, SwimMixin and FlyMixin,
and a Dragon class that inherits from both mixins.
while the Dragon class can perform additional actions.
"""


class SwimMixin:
    """
    A mixin class that provides swimming capabilities to an object.
    """

    def swim(self):
        """
        Method that prints "The creature swims!"
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying capabilities to an object.
    """

    def fly(self):
        """
        Method that prints "The creature flies!"
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    The Dragon class inherits from both SwimMixin and FlyMixin,
    enabling it to swim and fly. It also includes an additional
    ability to roar.
    """

    def roar(self):
        """
        Method that prints "The dragon roars!"
        """
        print("The dragon roars!")
