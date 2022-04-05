#!/usr/bin/env python
# coding: utf-8

# In[1]:


def isPermutation(stringOne, stringTwo):
    stringOne = sorted(stringOne)
    stringTwo = sorted(stringTwo)
    if len(stringOne) == len(stringTwo):
        for i in range(0, len(stringOne)):
            if stringOne[i] == stringTwo[i]:
                continue
        print("True")
    else:
        print("False")
        

isPermutation("Mamta", "atmam")


# In[ ]:




