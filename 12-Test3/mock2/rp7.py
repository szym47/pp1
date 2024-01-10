def f(n):
    if len(n)==4:
        suma=0
        arr=list(n)
        for i in arr[:-1]:
            suma+=int(i)
        if suma%7==int(n[3]):
            return True
    return False
    
print(f('1082'))
print(f('2035'))
print(f('1114'))
print(f('7071'))
print(f('704'))
print(f('704451'))