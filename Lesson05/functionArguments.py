# create a fancy greeting function that makes output like this:
def fancy_greeting(name):
    print('#############################')
    print('##-------------------------##')
    print('##' + name.center(25, '-') + '##')
    print('##-------------------------##')
    print('#############################')


# create an advanced version of this function with default arguments

def advanced_greeting(name, length=20, s='#'):
    print(length * s)
    print(s * 2 + (length - 4) * '-' + s * 2)
    print(s * 2 + name.center(length - 4, '-') + s * 2)
    print(s * 2 + (length - 4) * '-' + s * 2)
    print(length * s)


fancy_greeting('Sanjin')
advanced_greeting('Anna')
