months = ['January',  # 'JAN'
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

# 1. Lambda function calculating kinetic energy Ke = (m*v**2)/2
kinetic_energy = lambda m, v: (m * v ** 2) / 2
print('Kinetic energy:', kinetic_energy(85, 20), 'Joules')

# 2. Lambda function calculating energy in E = Mc**2
mass_energy = lambda m, c=299792458: m * c ** 2
print('Mass energy:', mass_energy(0.00000002), 'Joules')

# 3. Lambda function calculating gravitational force F = G*m1*m2/r**2
gravitational_force = lambda m1, m2=5.972 * 10 ** 24, r=6371000: 6.67408 * 10 ** -11 * m1 * m2 / r ** 2
print('My gravitational force', gravitational_force(84, 62, 2), 'Newtons')

# 4. Lambda function creating abbreviation for each month from a list
abv_months = list(map(lambda month: month[:3].upper(), months))

print(abv_months)
print(type(abv_months))
print(type(mass_energy))
