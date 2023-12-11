def f(years, course):
    import json
    with open('data.json', 'r') as file:
            data = json.load(file)
    for students in data:
          