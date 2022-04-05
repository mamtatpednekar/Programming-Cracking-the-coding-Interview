#!/usr/bin/env python
# coding: utf-8

# In[1]:


def oneAway(stringOne, stringTwo):
    ctr = 0
    if len(stringOne) - len(stringTwo) == 1:
        print(True)
    if len(stringOne) - len(stringTwo) == 0:
        stringOne = sorted(stringOne)
        stringTwo = sorted(stringTwo)
        for i in range(0, len(stringOne)):
            if stringOne[i] != stringTwo[i]:
                ctr = ctr+1
        if ctr > 1:
            print(False)
        else:
            print(True)
    else:
        print(False)
    
oneAway("Hi","Ho")
oneAway("Monday", "Tuesday")


# In[ ]:




