from collections import OrderedDict

a = OrderedDict(name='Zeus', role='god', home='Olympus')
b = {}
dictionary_functions = dir(b)
OrderedDict_functions = dir(a)

#print(dictionary_functions)

for f in OrderedDict_functions:
    if f not in dictionary_functions:
        print(f)
