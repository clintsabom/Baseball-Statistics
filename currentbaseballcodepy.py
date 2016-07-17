
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np







# In[ ]:




# In[2]:

import matplotlib.pyplot as plt
import pandas as pd




# In[4]:

baseball_df=pd.read_csv('Batting')





# In[5]:

baseball_df.describe()





 



# In[6]:

baseball_df.head()


# In[ ]:


   

   
   
   
   
   


# In[7]:

def correlation(x,y):
    std_x=(x-x.mean())/x.std(ddof=0)
    std_y=(y-y.mean())/y.std(ddof=0)
    
    return (std_x * std_y).mean()




# In[8]:

print correlation(baseball_df['2B'],baseball_df['HR'])





            







# In[9]:

print correlation(baseball_df['H'],baseball_df['HR'])




# In[10]:

print correlation(baseball_df['3B'],baseball_df['HR'])



# In[11]:

print correlation(baseball_df['SO'],baseball_df['HR'])




# In[12]:

get_ipython().magic(u'matplotlib inline')
df_num= baseball_df._get_numeric_data().copy()
ax=baseball_df.plot(x='yearID',y='HR',kind='scatter')
ax.set_xlabel('yearID')
ax.set_ylabel('HR')
ax.set_title('Total Homeruns By Year')
plt.savefig('Scatterplot')
df = pd.DataFrame([[.81,.81],[70,70]])
ax = df.plot.scatter(x=0, y=1, style='b')
df.plot.line(x=0, y=1, ax=ax, style='b')
ax.set_title('Total Homeruns By Year')
ax.set_xlabel('yearID')
ax.set_ylabel('HR')



















    








# In[13]:

get_ipython().magic(u'matplotlib inline')
df_num= baseball_df._get_numeric_data().copy()
ax=baseball_df.plot(x='HR',y='yearID',kind='hist')
plt.legend('#')
ax.set_xlabel('Year')
ax.set_ylabel('Total Homeruns Of All Major League Players')
ax.set_title('Total Homeruns By Years')
plt.savefig('Histogram')




















 






# In[14]:

print correlation(baseball_df['HBP'],baseball_df['HR'])


# In[15]:

df_num= baseball_df._get_numeric_data().copy()




# In[16]:

Baseballratio=df_num.astype('float').div(df_num['AB'].astype('float'),axis='index')








# In[17]:

print Baseballratio.ix[:20]


# In[18]:

print correlation(Baseballratio['2B'],Baseballratio['HR'])




# In[19]:

print correlation(Baseballratio['3B'],Baseballratio['HR'])


# In[20]:

baseball_df.apply(np.max)







# In[21]:

print correlation(Baseballratio['HBP'],Baseballratio['HR'])


# In[22]:

print correlation(Baseballratio['H'],Baseballratio['HR'])


# In[23]:

get_ipython().magic(u'matplotlib inline')
df_num= baseball_df._get_numeric_data().copy()
ax=baseball_df.plot(x='yearID',y='HR',kind='scatter')
ax.set_xlabel('yearID')
ax.set_ylabel('HR')
ax.set_title('Relationship between years and homeruns')
plt.savefig('Scatterplot')
df = pd.DataFrame([[.81,.81],[70,70]])
ax = df.plot.scatter(x=0, y=1, style='b')
df.plot.line(x=0, y=1, ax=ax, style='b')
ax.set_title('Relationship between years and homeruns')
ax.set_xlabel('yearID')
ax.set_ylabel('HR')


# In[ ]:




# In[24]:

Homeruns=baseball_df['HR']
ax=baseball_df.plot(x=1,y='HR',kind='box')
ax.set_xlabel('Homers')
ax.set_ylabel('General Range')
ax.set_title('Range of Homers hit by individual players in one season')

















# In[25]:

doubles_by_homerun_amount=baseball_df.groupby('HR').mean()['2B']
get_ipython().magic(u'pylab inline')
get_ipython().magic(u'matplotlib inline')
doubles_by_homerun_amount.plot(x='Homeruns Per Season',y='Doubles Per Season', kind='line')
ax.set_xlabel('Homeruns Per Season')
ax.set_ylabel('Doubles Per Season')
ax.set_title('Doubles Per Homerun')
plt.show()











# In[ ]:




# In[ ]:



