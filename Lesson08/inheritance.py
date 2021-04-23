class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print('meeeeooowwww')


class Leopard(Cat):
    def vocalize(self):
        print('wwgggghhrrr')


class Cheetah(Cat):
    def vocalize(self):
        print('eeeeeeeeee')


tommy = Cat(5, 17, 16)
tommy.vocalize()

leo = Leopard(90, 13, 27)
leo.vocalize()

mutombo = Cheetah(30, 15, 70)
mutombo.vocalize()

print(leo.__dict__)
