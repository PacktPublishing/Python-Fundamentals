try:
    house_value = 10000
    house_value[2] = 20000
    print(house_value)
    with open('input.txt', 'r') as myinputfile:
        print('how about here?')
        for line in myinputfile:
            print(line)
except FileNotFoundError:
    print('That file does not exist')
except NameError:
    print('An invalid name was used')
except TypeError:
    print('You treated an integer as if it was a list')
finally:
    print('I show up after every exception hahaha')

