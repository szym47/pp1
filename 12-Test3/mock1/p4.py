# (p4.py) The prods array contains the names of the products in stock. Create a function f(fnc,prods) that maps product names to their IDs, according to the fnc function. The f function returns a comma-separated list of product IDs, with no spaces. Example:
# prods = ["water","cheese","tomato"] 
# fnc1 = lambda x: "id:"+x[:2] 
# f(fnc1,prods) -> " id:wa,id:ch,id:to"
# fnc2 = lambda x: (x[0]+x[-1]).upper() 
# f(fnc2,prods) -> "WR,CE,TO"


def f(fnc, prods):
    x = list(map(fnc, prods))
    string = ''
    for item in x:
        string += item + ','
        
    return string

# Define lambda function separately
fnc1 = lambda x: "id:" + x[:2]
prods = ["water", "cheese", "tomato"]

# Call the function with the defined lambda function and prods
result1 = f(fnc1, prods)
print(result1)

# Define another lambda function separately
fnc2 = lambda x: (x[0] + x[-1]).upper()

# Call the function with the second defined lambda function and prods
result2 = f(fnc2, prods)
print(result2)
