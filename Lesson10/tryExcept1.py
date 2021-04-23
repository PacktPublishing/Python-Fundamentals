try:
    with open('input.txt', 'r') as myinputfile:
        print('how about here?')
        for line in myinputfile:
            print(line)
except FileNotFoundError:
    print('That file does not exist')

print('Execution never gets here')