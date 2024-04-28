#!/usr/bin/env python
# coding: utf-8



# In[270]:


iinput1 = input()
iinput2 = input()
iinput3 = input()


# In[271]:


waterlevel = [float(i) for i in iinput1.split(',')]
k1 = float(iinput2) 
k2 = float(iinput3)

if k1<1:
    k1 =2

if k2<1:
    k2 =2




# In[272]:


def is絕對遞增(llist):
    for i in range(1,len(llist)):
        if(llist[i-1]>=llist[i]):
            return False
        
    return True

def is絕對遞減(llist):
    for i in range(1,len(llist)):
        if(llist[i-1]<=llist[i]):
            return False
        
    return True


# In[273]:


answer = []
for i in range(0,len(waterlevel)):
    遞減uppbound = int( i+1)
    遞減llowerbound =int( max(0,i-k1) )

    遞增uppbound  = int( min(i+k2+1,len(waterlevel)))
    遞增llowerbound = int( i ) 
    
    # print(i, 遞減uppbound,遞減llowerbound)
    # print(i,遞增uppbound,遞增llowerbound)
    if(is絕對遞增(waterlevel[遞增llowerbound:遞增uppbound]) == True 
       and is絕對遞減(waterlevel[遞減llowerbound:遞減uppbound]) == True):
        if(i-k1 < 0):
            continue
        if(i+k2+1 > len(waterlevel)):
            continue
        answer.append(i)
answer


# In[274]:


if len(answer)==0 :
    print('NA')
else:
    for ele in answer:
        print(ele)


# In[275]:


# is絕對遞減(waterlevel[0:2])
# print( is絕對遞增(waterlevel[5:7]))
# print( is絕對遞減(waterlevel[4:6]))
# print(waterlevel[4:6])


# In[276]:


10,0 ,1,2,3,4,4,4
waterlevel[1:]


# In[277]:


# get_ipython().system('jupyter nbconvert --to script midterm2.ipynb')

