# (p1.py) Create a function f(n) that returns the difference between the largest and smallest odd digit contained in the number n. When the number n does not contain odd digits, the function returns -1. Example:
# f(10852) -> 4
# f(7235973) -> 6
# f(4388) -> 0
# f(846206) -> -1

def f(n):
    odd_digits=[]
    for index, digit in enumerate(str(n)): 
        if int(digit)%2!=0:
            odd_digits.append(digit)
    odd_digits = list(map(int, odd_digits))
    if odd_digits==[]:
        return -1
    return max(odd_digits)-min(odd_digits)

print(f(10852))    # 4
print(f(7235973))   # 6
print(f(4388))      # 0
print(f(846206))    # -1