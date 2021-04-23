numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
letters = ('a', 'b', 'c', 'd')

# slicing of tuples
print(numbers[2:5])
even_nums = numbers[1::2]
odd_nums = numbers[0::2]
print('even numbers', even_nums)
print('odd numbers', odd_nums)

# iteration with tuples
for n in numbers:
    print(n ** 2)


# functions with tuples
def area_and_circumference_of_circle(radius):
    import math
    return (math.pi * radius ** 2, 2 * math.pi * radius)


print(area_and_circumference_of_circle(9))
# common errors with tuples (assignment, iteration)
letters = letters + 'e'