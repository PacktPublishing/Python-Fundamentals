rainfall = [68, 58, 0, 99, 200, 39, 73, 43, 68, 0, 19]
location = 'Melbourne'

def print_rainfall(values):
    count = 1
    for value in values:
        print('Day',count,':',value)
        count += 1
    print(__name__)

def change_location(new_location):
    location = new_location
    print('the new location is:',location)
    print(__name__)

def rainy_day_count(values):
    count = 0
    for value in values:
        if value > 0:
            count += 1
    print(__name__)
    return count
