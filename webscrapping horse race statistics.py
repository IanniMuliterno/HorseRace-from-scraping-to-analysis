#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[5]:


response = requests.get('http://www.racebase.co.nz/jockthis.htm')


# ---
# HTML and XML specify their encoding, and we can use `content` to check that. you will see that we also have an attribute called `encoding`, but it just makes an educated guess on the encoding used, so it's nice to check

# In[8]:


response.content


# In[9]:


response.encoding


# In[11]:


soup = BeautifulSoup(response.text,'html.parser')


# # Just like what we see at browser inspect:

# In[12]:


print(soup.prettify())


# ---
# Now, there are two very helpful functions in `BeautifulSoup` that helps us navigate the html code, they're called `find` and `find_all` as their name suggests, with one, you can find the first occurrence of a tag, and with the other you get a list with every occurrence of that tag you're looking for. Knowing that, I've used find_all to get the third table in the site, in there I find the statistics table and we're going to need them in order to create our pandas version

# In[85]:


statistics_table = soup.find_all('table')[2]


# Using the same principle, lets go to the row where the table header is located

# In[86]:


statistics_table.find_all('tr')[1]


# In[96]:


table_titles = statistics_table.find_all('tr')[1]


# In[50]:


table_titles.text.strip()


# In[97]:


table_titles = [title.text.strip() for title in table_titles]


# In[98]:


table_titles


# In[99]:


#removing empty strings
table_titles = [title for title in table_titles if title != '']


# # Let's create our dataframe
# but before that, notice that the jockeys are ranked by victories, even so there's no nome on our rank column. Let's include that.

# In[100]:


table_titles.insert(0,'Rank')
statistics_df =  pd.DataFrame(columns=[table_titles])


# In[121]:


statistics_df


# In[61]:


#where is the data of our columns?
statistics_table.find_all('tr')[2]


# In[62]:


statistics_table.find_all('tr')[-1]


# In[63]:


column_data = statistics_table.find_all('tr')[2:]


# In[120]:


#let's go step by step, first, we need to go into each row and retrieve the text inside, use strip to grant there's no empty strings
# notice that we had to tidy in the same way we did with the title
for row in column_data:
    row_stripped = [row2.text.strip() for row2 in row]
    print([row3 for row3 in row_stripped if row3 != ''])


# In[147]:


#now we need to append it to the dataframe

for row in column_data:
    row_stripped = [row2.text.strip() for row2 in row]
    row_cleaned = [row3 for row3 in row_stripped if row3 != '']
    length = len(statistics_df)
    statistics_df.loc[length] = row_cleaned


# In[150]:


statistics_df

