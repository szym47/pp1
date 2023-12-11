def f(arr):
    import re
    valid=0
    for username in arr:
        if re.match('^[a-z0-9_]{4,12}$', username):
            valid+= 1
    return(valid)

if __name__== '__main__':
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))