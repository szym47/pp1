# (p3.py) Flight numbers along with the number of passengers are stored in a dictionary d. Define a function f(d) that returns the number of flights in which the number of passengers is greater than the average number of passengers on all flights. Example:
# f({"LO231":150,"BA787":120,"NZ15":30}) -> 2
# f({"LO231":150,"BA787":20,"NZ15":30}) -> 1


def f(d):
    average=sum(d.values())/len(d.values())
    count=0
    for key,value in d.items():
        if value>average:
            count+=1
    return count

print(f({"LO231": 150, "BA787": 120, "NZ15": 30}))   # 2
print(f({"LO231": 150, "BA787": 20, "NZ15": 30}))   