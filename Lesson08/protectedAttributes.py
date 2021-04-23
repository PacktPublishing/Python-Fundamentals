class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self._model = model
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self._model

    def get_year(self):
        return self.__year

    def set_model(self, new_model):
        self._model = new_model


my_car = Car('mazda', '6', 2010)
print(my_car._model)
my_car.set_model('6x')
print(my_car.get_make())

print(my_car.__dict__)
