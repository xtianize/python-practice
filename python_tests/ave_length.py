import math
import string

essay=input()
word_size=[]

def clean_essay(text:str)->str:
    translator=str.maketrans("","",string.punctuation)
    return text.translate(translator)

essay=clean_essay(essay)

words=essay.split()
for word in words:
    word_size.append(len(word))
ave_len = math.ceil(sum(word_size)/len(word_size))
print("average length:",ave_len)