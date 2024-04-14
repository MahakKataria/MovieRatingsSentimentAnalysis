#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np

df_IMDB = pd.read_csv('/Users/mahak/Library/CloudStorage/OneDrive-SanFranciscoStateUniversity/DS861/IMDB Dataset.csv')


# In[19]:

review = df_IMDB['review'].tolist()
print (len(review))


# In[20]:


positive_words= ['wonderful', 'incredible', 'amazing', 'great', 'captivating', 'best', 'beautiful', 'fantastic', 'favourite', 'top']
negative_words= ['worst', 'terrible', 'boring', 'awful', 'bad', 'mediocre', 'stale', 'uninspired', 'forgettable', 'dull'] 


# In[21]:


def contains(review, words):
    if any(word in review for word in words):
        return True
    return False


# In[22]:


num_positive_reviews=0
num_negative_reviews=0
for r in review:
    if contains (r, negative_words):
        num_negative_reviews = (num_negative_reviews + 1)
    else:
        num_positive_reviews = (num_positive_reviews + 1)
        
# if a review doesn't contain any negative word, it will be counted as positive.


# In[23]:

print (num_positive_reviews) 
print (num_negative_reviews)


# In[24]:


positive_review_fraction = (num_positive_reviews/len(review))
print (positive_review_fraction)


# In[25]:


negative_review_fraction = (num_negative_reviews/len(review))
print (negative_review_fraction)


# In[26]:


sentiment_score= (positive_review_fraction) - (negative_review_fraction)
print (sentiment_score)



# In[ ]:




