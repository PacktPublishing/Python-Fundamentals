class Person:
    def __init__(self, name, age, height_in_cm):
        self.name = name
        self.age = age
        self.height_in_cm = height_in_cm

    def speak(self):
        print(f'Hello! My name is {self.name}. I am {self.age} years  old.')

    def greet(self, person):
        if person.name == 'Rogers':
            print('Hey neighbour!')
        else:
            print(f'Hi {person.name}')


bob = Person('Bob', 33, 180)
sally = Person('Sally', 35, 160)

bob.greet(sally)

