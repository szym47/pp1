# 8.	Write a program that converts speed in meters per second
# to speed in kilometers per hour. Define a function ms_to_kmh(ms) 
# that returns the calculated speed in km/h. Sample result:
# 10 m/s = 36 km/h
# 35 m/s = 126 km/h)
n1 = 10
n2 = 35

def ms_to_kmh(ms):
    return int(ms*3.6)
    

print(ms_to_kmh(n1),ms_to_kmh(n2))