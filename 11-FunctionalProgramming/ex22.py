# 22.	The array below contains employee data: 
# [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
#  ("Jackson","Peter"),("Johnson","Rick"),
#  ("Lewis","Terry"),("Clarke","Robin")]
# Write a program that determines and displays a list
# of employees whose last names are given in capital letters
# followed by first names, separated by commas.
arr=[("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
 ("Jackson","Peter"),("Johnson","Rick"),
 ("Lewis","Terry"),("Clarke","Robin")]

#join to print under themselves
emp='\n'.join(list(map(lambda x: x[0].upper()+', '+x[1],arr)))
print(emp)

