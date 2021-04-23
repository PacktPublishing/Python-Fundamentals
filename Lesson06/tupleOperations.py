numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
letters = ('a', 'b', 'c', 'd')

# concatenation
print(numbers + letters)
# multiplication
print(letters * 2)

nested = (numbers, letters)
print(nested)
print(nested[1][2])

for num in numbers:
    if num % 2 == 0:
        print(num, 'is even')


even = numbers[1::2]
print(even)
odd = numbers[0::2]
print(odd)
even_under_5 = numbers[1:4:2]
print(even_under_5)
