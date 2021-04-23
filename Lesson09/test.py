# create a Python package by creating a folder in the current working directory
# access a python package via different import statement
from faveObjects.Car import *
from faveObjects import WebBrowser as wb

my_car = Car('mazda','6',2010,1500,220)
my_car.accelerate(25)
print(my_car.__dict__)
# use the classes in the package to create objects and perform operations

mozilla = wb.WebBrowser('google.com')
mozilla.navigate('facebook.com')
print(mozilla.__dict__)