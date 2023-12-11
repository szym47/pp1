def f(first_letter,last_letter):
    count=0
    with open('data.txt', 'r', encoding='UTF-8') as file:
        content = file.read()
        words= content.split()
        for word in words:
            if (word.lower()).startswith(first_letter) and (word.lower()).endswith(last_letter):
                count += 1
    print(count)
f("w","d") 