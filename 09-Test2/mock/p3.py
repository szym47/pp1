def f(array2D):
    rows=dict()
    i=1
    for x in array2D:
        z=0
        for y in x:
            z+=y
        rows[i] =rows.get(i,0)+z
        i+=1
    print(rows)

    #columns
    col=dict()
    o=1
    m=0
    for x in array2D:
        


f([[3,7,2],
   [4,2,5],
   [5,2,1]])