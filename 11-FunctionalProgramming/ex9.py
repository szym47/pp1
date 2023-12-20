# 9.	Write a program that converts speed in meters per second to speed 
# in kilometers per hour. Use an anonymous function. Sample result:
# 10 m/s = 36 km/h
# 35 m/s = 126 km/h
n1 = 10
n2 = 35
result = lambda n: n*3.6
print(f"{n1}m/s = {result(n1)}km/h \n{n2}m/s = {result(n2)}km/h")