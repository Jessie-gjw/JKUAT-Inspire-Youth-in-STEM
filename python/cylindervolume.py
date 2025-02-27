#Formula volume of a cylinder: V = πr^2h

import math
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: ")) 
print(cylinder_volume(radius, height))