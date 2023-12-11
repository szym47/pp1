def f(subjects):
    max_subject=''
    max_average=0
    for subject, grades in subjects.items():    
        average =sum(grades) / len(grades)
        if average>max_average:
            max_average=average
            max_subject=subject

    return max_subject

if __name__== '__main__':
    print(f({"math":[3,6,6,6,6,4,4],"geo":[5,4,4,4],"comp":[5,4]}) )
    