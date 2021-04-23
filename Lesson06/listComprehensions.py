"""
variableName = [operation    for loop    if statement(optional)]
"""

squares = [num ** 2 for num in range(1, 11)]
odd_squares = [num ** 2 for num in range(1, 11) if num ** 2 % 2 != 0]
even_squares = [num ** 2 for num in range(1, 11) if num ** 2 % 2 == 0]

print(squares)
print(odd_squares)
print(even_squares)