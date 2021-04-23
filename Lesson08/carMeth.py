class Car:
    def __init__(self, make, model, year, weight, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.max_speed = max_speed
        self.speed = 0

    def accelerate(self, add_speed=5):
        self.speed += add_speed
        if self.speed > self.max_speed:
            self.speed = self.max_speed


dream_car = Car('Dolorean', 'DMC', 1983, 1216, 180)
my_car = Car('mazda', '6', 2010, 1516, 220)
for i in range(0, 10):
    dream_car.accelerate(20)
    dream_car.accelerate(25)
print(dream_car.__dict__)

# create new attributes for speed (value not set via parameter) and max speed

# create an accelerate method with a default acceleraton
