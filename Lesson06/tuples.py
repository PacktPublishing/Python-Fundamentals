# create tuples
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
m = ('a', 23, 2.678)

# create nested or 2D tuples
two_dim = ((2, 3), (5, 3), (7, 2))

# access items from tuples and nested tuples
print(m[2])
print(two_dim[2][0])
print(two_dim[2][1])

# pack and unpack tuples
packing_tuple = 2, 5, 'Space'
print(packing_tuple)
a, b, c = packing_tuple
print(a)
print(b)
print(c)
print(packing_tuple)