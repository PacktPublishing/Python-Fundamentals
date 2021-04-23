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