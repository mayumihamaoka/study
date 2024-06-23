import pytest
from shapes.rectangle import Rectangle

def test_rectangle_area():
    rectangle = Rectangle(width=10, height=4)

    assert rectangle.area() == 40


print("Hello World")


