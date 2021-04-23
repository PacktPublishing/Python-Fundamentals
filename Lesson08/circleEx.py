import math


# Define the Circle class and the Circle constructor method
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def change_radius(self,new_radius):
        self.radius = new_radius

circle = Circle(1)
while True:
    radius = float(input('please enter radius:'))
    circle.change_radius(radius)
    print('Area:', circle.area())
    print('Circumference:', circle.circumference())

# Create the area calculation method, which returns the circle's area


# Create the circumference method, which returns the circle's circumference


# After the class definition, add the code that requests for user input for the radius


# Create a while loop requesting the user input, changing the circle object's radius and
# then printing out the area and circumference
