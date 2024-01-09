# (p6.py) A valid number on the planet Metis consists of digits 1 to 7 and lowercase or uppercase letters a to d. A plus (+) or minus (-) sign may also appear at the beginning of the number. The mnumbers array contains sample numbers. Create a function f(mnumbers) that returns how many numbers in the array that are valid in the planet Metis. Example:
# f(["A15","-31","7abC","+D1","-gH"]) -> 5
# f(["A05","-3+1","7ab8C","+D1","-22k"]) -> 1

# import re

# def f(mnumbers):
#     pattern = re.compile(r'^[+-]?[1-7a-dA-D]+$')
#     valid_count = sum(1 for num in mnumbers if pattern.match(num))

#     return valid_count

# # Example usage:
# result1 = f(["A15", "-31", "7abC", "+D1", "-gH"])
# print(result1)  # Output: 5

# result2 = f(["A05", "-3+1", "7ab8C", "+D1", "-22k"])
# print(result2)  # Output: 1


def f(mnumbers):
    import re
    result=re.match(r"^[-+]{1}[a-dA-D]$",mnumbers)
    return len(result)

print(f(["A15","-31","7abC","+D1","-gH"]))
print(f(["A05","-3+1","7ab8C","+D1","-22k"]))

