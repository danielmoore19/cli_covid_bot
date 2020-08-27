import pandas as pd
import nltk
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize


def get_wordnet_pos(word):
  #Map POS tag to first character lemmatize() accepts
  tag = nltk.pos_tag([word])[0][1][0].upper()
  tag_dict = {"J": wordnet.ADJ,
              "N": wordnet.NOUN,
              "V": wordnet.VERB,
              "R": wordnet.ADV}

  return tag_dict.get(tag, wordnet.NOUN)

def preprocess(docs):
  lemmer = WordNetLemmatizer()
  prepd = []

  for doc in docs:
    tokenized = word_tokenize(doc)

    cleaned = [lemmer.lemmatize(token.lower(), get_wordnet_pos(token))
               for token in tokenized
               #if token.lower() not in stopwords.words('english')
               if token.isalpha()]

    untokenized = ' '.join(cleaned)
    prepd.append(untokenized)

  return prepd

df = pd.read_csv('https://https://raw.githubusercontent.com/danielmoore19/cli_covid_bot/master/covid_df.csv?token=AMNBPP6KOWTXKUNOYIKWH5K7I7WMG')
lemm = preprocess(df['questions'])