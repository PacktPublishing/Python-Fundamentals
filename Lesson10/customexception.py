class RecipeNotValidError(Exception):
    def __init__(self):
        self.message = 'RecipeNotValidError'

try:
    recipe = 5656565
    if type(recipe) != str:
        raise RecipeNotValidError

except RecipeNotValidError as e:
    print(e.message)

print('Yay the code got to the end')