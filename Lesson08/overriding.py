class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print('meeeeooowwww')

    def __str__(self):
        return f'the {type(self).__name__.lower()} '\
               f'weighs {self.mass_in_kg}kg '\
               f'and lives for {self.lifespan_in_years} years '\
               f'and can run at a speed of {self.speed_in_kph}kph'


class Leopard(Cat):
    def __init__(self, mass, lifespan, speed,spotted = True):
        super().__init__(mass, lifespan, speed)
        self._spotted = spotted

    def vocalize(self):
        print('wwgggghhrrr')

    def __str__(self):
        if self._spotted == True:
            st = 'spotted '
        else:
            st = ''
        return f'the {st}{type(self).__name__.lower()} '\
               f'weighs {self.mass_in_kg}kg '\
               f'and lives for {self.lifespan_in_years} years '\
               f'and can run at a speed of {self.speed_in_kph}kph'


class Cheetah(Cat):
    def vocalize(self):
        print('eeeeeeeeee')


tommy = Cat(5, 17, 16)
tommy.vocalize()
print(tommy)

leo = Leopard(90, 13, 27,False)
leo.vocalize()
print(leo)

mutombo = Cheetah(30, 15, 70)
mutombo.vocalize()
