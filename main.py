#!/usr/bin/env python
# coding: utf-8


import streamlit as st

from textblob import TextBlob

import numpy as np
import pandas as pd
import string

# import neattext as nt
# import neattext.functions as nfx
# import re
# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
# import matplotlib.pyplot as plt
# import seaborn as sns

# import ipywidgets
# from ipywidgets import interact

# plt.rcParams['figure.figsize'] = (15, 5)
# plt.style.use('fivethirtyeight')

# reading the Dataset
data = pd.read_csv('drug.csv')


def punctuation_removal(messy_str):
    clean_list = [char for char in messy_str if char not in string.punctuation]
    clean_str = ''.join(clean_list)
    return clean_str


data['review'] = data['review'].apply(punctuation_removal)

# data['review']=data['review'].apply(nfx.remove_currency_symbols)
# data['review']=data['review'].apply(nfx.remove_stopwords)
# data['review']=data['review'].apply(nfx.remove_numbers)
# data['review']=data['review'].apply(nfx.remove_currencies)
# data['review']=data['review'].apply(nfx.remove_bad_quotes)
# data['review']=data['review'].apply(nfx.remove_special_characters)

# lets calculate the Sentiment from Reviews

# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# sid = SentimentIntensityAnalyzer()

# train_sentiments = []

# for i in data['review']:
#     train_sentiments.append(sid.polarity_scores(i).get('compound'))

# train_sentiments = np.asarray(train_sentiments)
# data['sentiment'] = pd.Series(data=train_sentiments)


# lets remove the unique Id, date, review, len, and sentiment column also
# data = data.drop(['date','uniqueID','sentiment','review','len'], axis = 1)


st.title('IOU PROJECT by Abideen')
st.sidebar.write('Welcome to my page')
st.sidebar.button('click me')

condition = st.text_input("Enter your medical condition: ")

drug = st.text_input("What drug was described for you by a doctor?: ")

review = st.text_input(f"What is your review on {drug}? ")

text = "This is a great movie! I love it."
sentiment = TextBlob(text).sentiment

st.write(sentiment)
# output Sentiment(polarity=0.8, subjectivity=0.75)
