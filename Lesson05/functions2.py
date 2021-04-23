def hello10():
    print('function is from',__name__)
    print('Hello ' * 10)

def pyramid(layers):
    print('function is from', __name__)
    star = '*'
    for i in range(0, layers):
        print(star.center(layers * 2, ' '))
        star += '**'

def circle_area(radius):
    print('function is from', __name__)
    import math
    return math.pi * radius ** 2

def surface_area_cuboid(l, w, h):
    """This function takes in length, width and height of a cuboid and returns the surface area."""
    print('function is from', __name__)
    return 2 * (l * w + w * h + l * h)

if __name__ == '__main__':
    hello10()
    pyramid(8)
    print(circle_area(5))
    print(surface_area_cuboid(3, 5, 7))
    print(surface_area_cuboid.__doc__)