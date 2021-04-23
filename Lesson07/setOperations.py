a = {1, 2, 3}
b = {3, 4, 5}

# A union B
print('a union b')
print(a.union(b))
print(a | b)

# A intersection B
print('a intersection b')
print(a.intersection(b))
print(a & b)
# A equals to B
print(a == b)

# Subsets and supersets
print('subsets and supersets')
print(a.issubset(b))
print(b.issuperset(a))
b.update(a)
print(b)
print(a.issubset(b))
print(b.issuperset(a))


