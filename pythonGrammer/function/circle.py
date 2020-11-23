#!/usr/bin/env python
# coding: utf-8

# In[1]:


pi = 3.14159

# In[ ]:


def area(r):
    return pi*(r**2)

def circumference(r):
    return 2*pi*r

def sphereSurface(r):
    return 4*area(r)

def sphereVolume(r):
    return (4.0/3.0)*pi*(r**3)

