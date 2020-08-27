import pandas as pd
import numpy as np
import preprocess
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('covid_df.csv')
lemm = preprocess.preprocess(df['questions'])
model = TfidfVectorizer()
tfidf = model.fit_transform(lemm).toarray()

def COVID2bot(user_response):
  text = model.transform([user_response]).toarray()
  df['similarity'] = cosine_similarity(tfidf, text)
  scores = df.sort_values(['similarity'], ascending=False)
  if scores.iloc[0]['similarity'] >= 0.8:
    return (scores.iloc[0]['answers'])
  else:
    first = scores.iloc[0]['questions']
    second = scores.iloc[1]['questions']
    third = scores.iloc[2]['questions']
    user_input = input(
        f'These are the top 3 matches to your question:\n1. "{first}"\n2. "{second}"\n3. "{third}"\nPlease type the number that matches your question, or hit return to ask a different question.\n')
    if user_input == '1':
      return (scores.iloc[0]['answers'])
    elif user_input == '2':
      return (scores.iloc[1]['answers'])
    elif user_input == '3':
      return (scores.iloc[2]['answers'])
    else:
      return ('Please ask another question.')