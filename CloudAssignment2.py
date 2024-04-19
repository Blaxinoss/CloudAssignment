#!/usr/bin/env python
# coding: utf-8

# In[9]:


import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords

from nltk.tokenize import sent_tokenize, word_tokenize



mytxt = open("random_paragraphs.txt").read().lower()

stoppingwords = set(stopwords.words("english"))
 # stoppingwordsarabic = set(stopwords.words("Arabic"))

# print(stoppingwordsarabic)
# print (stoppingwords)
        
allwords= word_tokenize(mytxt)


NoStoppingTxt = [w for w in allwords if w not in stoppingwords]


# print(NoStoppingTxt[0:100])

visitedCount = {}

for word in NoStoppingTxt :
    if word in visitedCount:
        visitedCount[word] +=1
    else :
        visitedCount[word] = 1
        
for w,c in visitedCount.items() :
    print("number of occurrence for the word", w, "=", c)


# In[ ]:




