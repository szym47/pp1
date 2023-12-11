def f(subjects):
    for subject, grades in subjects.items():
        averages = sum(grades) / len(grades)

    max_subject = max(averages, key=averages.get)
    
    return max_subject

f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}) 
    