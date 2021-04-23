def hello10():
    print('Hello ' * 10)

def pyramid(layers):
    star = '*'
    for i in range(0, layers):
        print(star.center(layers * 2, ' '))
        star += '**'

def circle_area(radius):
    import math
    return math.pi * radius ** 2

def surface_area_cuboid(l, w, h):
    """This function takes in length, width and height of a cuboid and returns the surface area."""
    return 2 * (l * w + w * h + l * h)


hello10()
pyramid(8)
print(circle_area(5))
print(surface_area_cuboid(3, 5, 7))
print(surface_area_cuboid.__doc__)