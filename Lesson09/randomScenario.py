import random

"""
You need to write a function that returns a randomly generated list of 30 floating point values each one being between
1.10 and 1.45
"""

def petrol_vals():
    possiblePrices = []
    price = 1.10
    output =[]
    while price <= 1.45:
        price += 0.01
        possiblePrices.append(round(price,2))
    for i in range(0,30):
        output.append(random.choice(possiblePrices))
    return output

def petrol_vals2():
    output = []
    for i in range(0,30):
        output.append(random.randint(110,145) / 100)
    return output




print(petrol_vals2())