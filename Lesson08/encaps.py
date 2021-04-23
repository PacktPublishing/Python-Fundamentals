class Car:
    def __init__(self, make, model, year):
        self._make = make
        self.__model = model
        self.__year = year

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        self.__model = new_model


my_car = Car('mazda', '6', 2010)
my_car._make = "Lotus"
my_car._Car__model = 'Whatever'
print(my_car.__dict__)
