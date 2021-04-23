sentence = 'Have a nice day'
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
letters = ('a', 'b', 'c', 'd')

for c in sentence:
    print(c.upper())

for num in numbers:
    print('square of', num, 'is', num ** 2)

for letter in letters:
    print(letter.center(11,'_'))
