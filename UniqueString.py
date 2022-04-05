#!/usr/bin/env python
# coding: utf-8

# In[1]:


def isStringUnique(stringOne):
    newString = set(stringOne)
    if len(stringOne) == len(newString):
        print(True)
    else:
        print(False)
        
        

isStringUnique("Atmosphere")


# In[ ]:




