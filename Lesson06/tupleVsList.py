import time

# list of squares of the first 10,000,000 numbers
list_squares = [num ** 2 for num in range(1, 10000000)]
# tuple of squares of the first 10,000,000 numbers
tup_squares = tuple([num ** 2 for num in range(1, 10000000)])

total = 0
tic = time.clock()
for num in list_squares:
    total += num
toc = time.clock()
print(total)
print('LIST time taken in seconds', toc - tic)

total = 0
tic = time.clock()
for num in tup_squares:
    total += num
toc = time.clock()
print(total)
print('TUPlE time taken in seconds', toc - tic)
