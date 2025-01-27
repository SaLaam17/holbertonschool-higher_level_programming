#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(5)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)
try:
    print(my_square_1._Square__size)
except Exception as e:
    print(e)
    
my_square_2 = Square(7)
print("Area: {}".format(my_square_2.area()))
try:
    print(my_square_2._Square__size)
except Exception as e:
    print(e)
