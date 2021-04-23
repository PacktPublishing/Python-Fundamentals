from collections import OrderedDict

a = OrderedDict(name='Zeus', role='god', age='old')
b = OrderedDict(name='Zeus', age='old', role='god')

print(a == b)

c = {'name': 'Zeus', 'role': 'god', 'age': 'old'}
d = {'age': 'old', 'name': 'Zeus', 'role': 'god'}

print(a == c)

print(c == d)
