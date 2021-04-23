rainfall = [68, 58, 0, 99, 200, 39, 73, 43, 68, 0, 19]
location = 'Melbourne'


def print_rainfall(values):
    day = 1
    for value in values:
        print('Day', day, ':', value)
        day += 1

def average_rainfall(values):
    import math
    return math.fsum(values) / len(values)

def change_location(new_location):
    global location
    location = new_location
    print('the new location is',location)

print_rainfall(rainfall)
print(average_rainfall(rainfall))
print(location)
change_location('New York')
print(location)