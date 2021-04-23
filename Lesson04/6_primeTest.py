import time

num = int(input('Provide a number to test:'))
tic = time.clock()
prime = True

for i in range(2, num):
    # if you can divide num by i and get no remainder
    # then num has a factor and is not a prime
    if num % i == 0:
        prime = False

toc = time.clock()
print('time taken:',toc-tic)

if prime == True:
    print(num, 'is a prime number')
else:
    print(num, 'is not a prime number')
