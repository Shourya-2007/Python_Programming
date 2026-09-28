#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(1, 11):
    print(i)


# In[3]:


for i in range(2, 21, 2):
    print(i)


# In[4]:


sum = 0
for i in range(1, 101):
    sum = sum + i
print("Sum =", sum)


# In[5]:


numbers = [10, 20, 30, 40, 50]
for i in numbers:
    print(i)


# In[6]:


num = int(input("Enter a number:"))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)

