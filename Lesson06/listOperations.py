numbers = [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]
letters = ['a', 'b', 'c', 'd', 'e']

# add lists
mix = letters + numbers
letters += numbers
print(mix)
print(letters)
# read index of lists
print(letters[2])
# read index of nested lists
print(letters[10][1])
# write items into lists and nested lists
letters[4] = 'E'
print(letters)
letters[10][1] = 700
print(letters)