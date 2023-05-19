import math

class Line:
    def __init__(self, length):
        self._length = length

    def set_length(self, length):
        self._length = length

    def get_length(self):
        return self._length

def area_square(length):
    return length * length

def area_regular_triangle(length):
    return length * length * math.sqrt(3) / 4

def area_circle(length):
    return length * length * math.pi

myline = Line(10)

square = area_square(myline.get_length())
print(square)

myline.set_length(20)
regular_triangle = area_regular_triangle(myline.get_length())
print(regular_triangle)

myline.set_length(30)
circle = area_circle(myline.get_length())
print(circle)
