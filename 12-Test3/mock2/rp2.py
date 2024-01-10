def f(arr):
    for i in arr:
        if arr.count(i)%2!=0:
            return i




print(f([2,2,2,2,3,3,3,5,5,5,5]))