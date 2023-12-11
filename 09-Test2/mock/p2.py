def f(arr):
    a = dict()
    for i in arr:
        a[i] =a.get(i,0)+1
    for key, count in a.items():
        if count == 1:
            return key
        

if __name__== '__main__':
    print(f(([7,7,7,7,7,7,7,5])))
