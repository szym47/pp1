# 24.	The educational course finished with a test checking
#  the participants' knowledge. Here are the results obtained
#  by the students:
# [37,51,44,23,78,92,39,84,83,51]
# Write a program that calculates and displays student scores
# that are equal to or greater than the following minimum 
# number of points to pass the course:
# a.	70
# b.	40
# c.	30
# Use the filter() function and the following higher order 
# function:
# def min_pts(limit):
#     return lambda pts: pts>=limit
arr=[37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
    return list(filter(lambda pts: pts>=limit,arr))

print('Min 70 pts: ',min_pts(70))
print('Min 40 pts: ',min_pts(40))
print('Min 30 pts: ',min_pts(30))