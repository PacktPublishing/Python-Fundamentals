# create the __init__ function for class car
class Car:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight


# initialise the car with attributes for make, model, year and weight
my_car = Car('mazda', '6', 2010, 1510)
dream_car = Car('Delorean', 'DMC', 1983, 1300)
# print the car object and its attributes

print(my_car.__dict__)
print(dream_car.__dict__)
print('my dream car is',dream_car.make,dream_car.model)