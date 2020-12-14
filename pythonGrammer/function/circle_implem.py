#!/usr/bin/env python
# coding: utf-8

# In[2]:


import circle


# In[ ]:


pi = 3# 对于circle内部模块而言，这里的pi属于外部变量，不会对circle内部模块的pi变量造成影响
print('pi is',pi)
print('cicle.pi',circle.pi)
print('circle.area',circle.area(3))
print('circle.circumference',circle.circumference(pi))
print('circle.sphereSurface',circle.sphereSurface(pi))

