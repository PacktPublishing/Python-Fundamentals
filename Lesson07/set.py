# create 2 sets
a = {1,2,3}
b = {3,4,5}

# print elements
print(a)
# iterate through sets
for item in a:
    print(item)
# add elements
a.add(4)
print(a)
a.update(b)
print(a)
# remove items from sets 3 different ways
a.remove(5)
a.discard(4)
print(a.pop())
print(a)