print('Please enter a number')
num = int(input())

# candidate will change in the while loop
# candidate is a potential factor
candidate = 1

while candidate <= num:
    # if num divided by candidate has no remainder
    if num % candidate == 0:
        print(candidate, 'is a factor of', num)
    candidate += 1
