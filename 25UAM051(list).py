#!/usr/bin/env python
# coding: utf-8

# List

# In[2]:


fruits = ["apple", "mango", "banana"]
print(fruits)


# In[3]:


print(fruits[1])


# In[4]:


print(fruits[1:3])


# In[5]:


print(len(fruits))


# In[11]:


fruits = ["apple", "mango", "banana"]
fruits.append("papaya")
print(fruits)
#append -> adds elements at the end of the list.


# In[12]:


print(type(fruits))


# In[16]:


fruits = ["apple", "mango", "banana"]
fruits.remove("mango")
print(fruits)
#remove -> to remove elements form list.


# In[17]:


fruits = ["apple", "mango", "banana"]
fruits.sort()
print(fruits)
#sort() -> sorts elements in ascending order.


# In[20]:


fruits = ["apple", "mango", "banana"]
fruits.sort(reverse = True)
print(fruits)
#sort(reverse = True) -> sorts elements in descending order.


# In[25]:


fruits = ["apple", "mango", "banana"]
fruits.extend(["cherry", "orange"])
print(fruits)
#extend -> adds multiple elements in the list.


# In[27]:


fruits = ["apple", "mango", "banana"]
fruits.insert(1, "cherry")
print(fruits)
#insert -> to insert element at specific position.


# In[ ]:




