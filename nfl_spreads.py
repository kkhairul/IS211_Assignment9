#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request
import sys
from bs4 import BeautifulSoup


# In[2]:


url = "http://www.footballlocks.com/nfl_point_spreads.shtml"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")


# In[3]:


find_table = soup.find_all('table', attrs = {'cols': '4', 'width': '580', 'cellspacing': '6', 'cellpadding': '3', 'border': '0'})


# In[4]:


for i in find_table:
    table = i


# In[5]:


tRows = table.find_all('tr')


# In[6]:


for i in tRows:
    tData = i.find_all('td')
    timedat = str(tData[0].get_text())
    favo = str(tData[1].get_text())
    spr = str(tData[2].get_text())
    udog = str(tData[3].get_text())


# In[7]:


print('Time/Date:{}, Favorite:{}, Spread:{}, Underdog:{}'.format(timedat, favo, spr, udog))


# In[ ]:




