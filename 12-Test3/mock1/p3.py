# (p3.py) The uid array contains user IDs in one of the popular websites. Identifiers should be unique. Create a function f(uid) that returns true if all ids are unique. Otherwise, the function returns false. Example:
# f(["john5","ann123","JOHN5","xxx","abc333","a10"]) -> True
# f(["abc123","ann","abc123","a10"]) -> False
# f(["bob2","bob2"]) -> False
# f(["bob2","BOB2"]) -> True

def f(uid):
    d={}
    for i in uid:
        d[i] = d.get(i, 0) + 1
    for x in d.values():
        if x==2:
            return False
    return True


print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["abc123","ann","abc123","a10"]))
print(f(["bob2","bob2"]))
print(f(["bob2","BOB2"]))