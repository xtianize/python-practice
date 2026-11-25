import math
import string

essay=input()
word_size=[]
punc=['.','']

filtered_essay=[char for char in essay if char not in string.punctuation]
text="".join(filtered_essay)
words=text.split()
for word in words:
    word_size.append(len(word))
ave_len = math.ceil(sum(word_size)/len(word_size))
print("average length:",ave_len)