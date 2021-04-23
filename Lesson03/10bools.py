raining = True
daytime = True
hot_outside = False

raining = not raining

if daytime and not raining and not hot_outside:
    print('Its a nice day lets go out')

if raining and not hot_outside or not raining and hot_outside:
    print('lets stay in')

if raining and hot_outside:
    print('lets dance in the rain')