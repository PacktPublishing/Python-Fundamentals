# create a car class
class Car():
    pass


# create a car object
honda = Car()
mazda = Car()

# add attributes to the car object
honda.model = 'CRV'
honda.weight = 1200

# print attributes in 2 different ways
print('Honda model:', honda.model)
print('Honda weight:', honda.weight)
print(honda.__dict__)
print(mazda.__dict__)