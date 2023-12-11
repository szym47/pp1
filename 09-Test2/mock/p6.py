def f(years, course):
    import json
    with open('data.json', 'r',encoding='utf-8') as file:
        data = json.load(file)
        count=0
        for student in data:
                if student["age"] >= years:
                        for courses in student["studies"]["courses"]:
                                if courses["name"] == course:
                                        if sum(courses["grades"]) / len(courses["grades"]) >= 4:
                                                count+=1
    return(count)


if __name__== '__main__':
    print(f(21,"statistics"))
