#!/usr/bin/env python
# coding: utf-8

# In[70]:


import re


# In[71]:


百家姓 = '陳林黃張李王吳劉蔡楊許鄭謝郭洪曾邱廖賴周徐蘇葉莊呂江何蕭羅高簡朱鍾施游詹沈彭胡余盧潘顏梁趙柯翁魏方孫戴范宋鄧杜侯曹薛傅丁溫紀蔣歐藍連唐馬董石卓程姚康馮古姜湯汪白田涂鄒巫尤鐘龔嚴韓黎阮袁童陸金錢邵'
綴詞列表 =['先生','小姐','姓']


# In[72]:


iinput = '黃姓記者表示：昨日，一家位於市中心的銀行被一伙歹徒搶劫。據警方報告，這伙歹徒是由五個陳姓男子、兩個林姓男子和七個黃姓女子組成的。搶劫發生時，銀行內只有幾名員工和幾名顧客。警方表示，這伙歹徒經過周密計劃，利用先前在銀行內工作的一名黃姓女子的幫助，成功地打開了銀行保險箱並搶走了大量現金和貴重物品。在搶劫過程中，他們使用了槍支和刀具，並對銀行內的員工和顧客進行了威脅和攻擊。當地警方接到報案後立即展開調查，通過監視器的錄像和目擊者提供的線索，成功地鎖定了這伙歹徒的身份。在警方的大力打擊下，其中一名姓陳的男子在逃亡途中被捕，並向警方供出了整個犯罪集團的情況和躲藏地點。隨後，警方成功地逮捕了其他幾名犯罪嫌疑人。目前，這伙搶劫犯罪集團已被依法拘留，案件正在進一步調查之中。市民們紛紛對警方的迅速反應和有效打擊表示贊揚，並期望警方能夠繼續加強打擊犯罪的力度，維護社會的安全和穩定。對此，一名姓林的市民表示：「真是太安心了！」'
iinput = input()

# In[73]:


單姓位置 = []

for i in 綴詞列表:
    iter = re.finditer( i  , iinput)
    indices = [m.start(0)-1 for m in iter]
    單姓位置+= indices
    iter = re.finditer( i  , iinput)
    indices = [m.start(0)+1 for m in iter]
    單姓位置+= indices

單姓位置


# In[74]:


百姓才會出現的單姓 = []

for ele in 單姓位置:
    if(iinput[ele] in 百家姓):
        百姓才會出現的單姓.append(iinput[ele])
百姓才會出現的單姓


# In[75]:


# 統計各個元素所用

x= [百姓才會出現的單姓.count(i) for i in set(百姓才會出現的單姓)]
y = set(百姓才會出現的單姓)




lastnameTofreq = dict(zip(y,x))


# In[76]:


lastnameToindex = []
for i in y:
    lastnameToindex.append(百家姓.index(i))
lastnameToindex


# In[77]:


最後的資料結構 = []

for i in range(len(lastnameToindex)):
    # print(list(lastnameTofreq.keys())[i] , list(lastnameTofreq.values())[i]  ,lastnameToindex[i] )
    最後的資料結構.append([list(lastnameTofreq.keys())[i] , list(lastnameTofreq.values())[i]  ,lastnameToindex[i] ])
最後的資料結構    


# In[ ]:




# In[78]:


最後的資料結構 = sorted(最後的資料結構,key=lambda data:(-data[1],data[2]))


# In[80]:


for ele in 最後的資料結構:
    print(f'{ele[0]}:{ele[1]}')


# 
