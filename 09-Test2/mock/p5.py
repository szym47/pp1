import re
def f(first_letter,last_letter):
    with open('data.txt','r', encoding='utf-8')as f:
        f_content=f.read()
        list_of_words=re.findall(fr'\b{first_letter}\w+{last_letter}\b',f_content)
        return len(list_of_words)

if __name__== '__main__':
    print(f("w","d"))