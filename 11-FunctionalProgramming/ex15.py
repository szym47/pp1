text='I completely agree with you'
spltext= text.split()
result=list(map(lambda x:len(x),spltext))
print(f'''
Text: I completely agree with you
No. of letters in words: {result}
''')