# 18.A speed camera located in a city measures the speed of
# passing vehicles. The maximum permitted speed of vehicles is
# 50 km/h. In the last minute, the speed camera recorded the
# following values: 48,47,54,50,42,68,39,46
# Write a program that displays speed values higher than the
# allowed speed. Use anonymous and filter() functions.
vmax=50
v=[48,47,54,50,42,68,39,46]
result=list(filter(lambda x:x>vmax,v))

print(f'''Recorded values: {v}
Speed too high:{result}''')