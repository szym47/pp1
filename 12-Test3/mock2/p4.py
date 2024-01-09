# (p4.py) The res array contains test results, i.e. the number of points between 0 and 100. Create a function f(fnc,res) that filters the test results according to the criteria contained in the fnc function. The f function returns the difference between the highest and lowest test result. Example:
# res = [95,90,20,50,70] 
# fnc1 = lambda x: x>50
# f(fnc1,res) -> 25
# fnc2 = lambda x: x>30 and x<90
# f(fnc2,res) -> 20

def f(fnc,res):
    filtered=list(filter(fnc,res))
    return max(filtered)-min(filtered)



res = [95,90,20,50,70] 
fnc1 = lambda x: x>50
print(f(fnc1,res))
fnc2 = lambda x: x>30 and x<90
print(f(fnc2,res))