# create a dictionary in 2 different ways
scores = dict(
    Bob=20,
    Alice=23
)

nicknames = {'Bob': 'Bobby', 'Alice': 'Ally'}

# print dictionary
print(scores)
print(nicknames)
# read a specific value from a dictionary
print(scores['Alice'])
scores['Cam'] = 22
scores['Cam'] += 1
print(scores)
# write a specific value to a dictionary
