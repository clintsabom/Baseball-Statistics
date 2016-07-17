
# coding: utf-8

# In[49]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def load_dataframe(path):
    df=pd.read_csv(path)
    return df

def correlation(x,y):
    std_x=(x-x.mean())/x.std(ddof=0)
    std_y=(y-y.mean())/y.std(ddof=0)

    return (std_x * std_y).mean()

def print_correlations(baseball_df, key):
    print correlation(baseball_df['2B'],baseball_df[key])
    print correlation(baseball_df['H'],baseball_df[key])
    print correlation(baseball_df['3B'],baseball_df[key])
    print correlation(baseball_df['SO'],baseball_df[key])


# In[50]:

baseball_df=load_dataframe('Batting.csv')
baseball_df.describe()
baseball_df.head()


# In[51]:

print_correlations(baseball_df, 'HR', )


# In[52]:


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

get_ipython().magic(u'matplotlib inline')
df_num= baseball_df._get_numeric_data().copy()
ax=baseball_df.plot(x='HR',y='yearID',kind='hist')
plt.legend('#')
ax.set_xlabel('Year')
ax.set_ylabel('Total Homeruns Of All Major League Players')
ax.set_title('Total Homeruns By Years')
plt.savefig('Histogram')

print correlation(baseball_df['HBP'],baseball_df['HR'])
df_num= baseball_df._get_numeric_data().copy()

Baseballratio=df_num.astype('float').div(df_num['AB'].astype('float'),axis='index')

print Baseballratio.ix[:20]
print correlation(Baseballratio['2B'],Baseballratio['HR'])
print correlation(Baseballratio['3B'],Baseballratio['HR'])

baseball_df.apply(np.max)

print correlation(Baseballratio['HBP'],Baseballratio['HR'])
print correlation(Baseballratio['H'],Baseballratio['HR'])

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
Homeruns=baseball_df['HR']
ax=baseball_df.plot(x=1,y='HR',kind='box')
ax.set_xlabel('Homers')
ax.set_ylabel('General Range')
ax.set_title('Range of Homers hit by individual players in one season')
doubles_by_homerun_amount=baseball_df.groupby('HR').mean()['2B']
get_ipython().magic(u'pylab inline')
get_ipython().magic(u'matplotlib inline')
doubles_by_homerun_amount.plot(x='Homeruns Per Season',y='Doubles Per Season', kind='line')
ax.set_xlabel('Homeruns Per Season')
ax.set_ylabel('Doubles Per Season')
ax.set_title('Doubles Per Homerun')
plt.show()



# In[ ]:



