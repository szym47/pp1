# (p7.py) Create a function f(arr2D) that returns true when the sum of the values in at least two columns is the same. Otherwise, the function returns false. Example:
# f([[3,4,2],[5,1,6]]) -> True
# f([[3,4,2],[5,1,7]]) -> False
# f([[3,4],[5,1],[4,7]]) -> True
# f([[3,4],[5,9],[4,7]]) -> False

def f(arr2D):
    d={}
    for x in range(len(arr2D)):
        for y in range(len(arr2D[x])):
            d[y]=d.get(y,0)+arr2D[x][y]
    lista=[]
    for i in d.values():
        lista.append(i)

    seen_values = []

    for element in lista:
        if element in seen_values:
            return True
        seen_values.append(element)

    return False
    
    


print(f([[3,4,2],
         [5,1,6]]))

print(f([[3,4,2],
         [5,1,7]]))

print(f([[3,4],
         [5,1],
         [4,7]]))

print(f([[3,4],
         [5,9],
         [4,7]]))