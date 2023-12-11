def f(array2D):
    rows_num=len(array2D)
    for row_num in range(0,rows_num):
        row_sum=sum(array2D[row_num])
        col_sum=0
        for col_num in range(rows_num):
            col_sum+=array2D[col_num][row_num]
        if row_sum!=col_sum:
            return False
    return True


if __name__== '__main__':
    print(f([
    [3,7,2],
    [4,2,5],
    [5,2,1]]))

    print(f([
    [3,7,2],
    [4,2,5],
    [9,2,1]]))