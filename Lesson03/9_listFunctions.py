rainfall = [68, 58, 0, 99, 200, 39, 73, 43, 68, 0, 19]

min_rainfall = min(rainfall)
max_rainfall = max(rainfall)
average_rainfall = sum(rainfall) / len(rainfall)

print('minimum rainfal:', min_rainfall)
print('maximum rainfal:', max_rainfall)
print('average rainfall:', average_rainfall)
print(sorted(rainfall,reverse=True))
