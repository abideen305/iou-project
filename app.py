# !/usr/bin/env python
# coding: utf-8
import pandas as pd
import streamlit as st
import string
from textblob import TextBlob
import spacy
# import neattext as nt
# import neattext.functions as nfx
import re
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        label = "Positive"
        return label
    elif sentiment == 0:
        label = "Neutral"
        return label
    else:
        label = "Negative"
        return label


# def sentiment_analysis(text):
#     if "not" in text:
#         return "Negative"
#     elif "good" in text or "great" in text or "excellent" in text:
#         return "Positive"
#     else:
#         return "Neutral"


# reading the Dataset
df = pd.read_csv('drug.csv')
data = df[['drugName', 'review', 'condition', 'usefulCount']]


def punctuation_removal(messy_str):
    clean_list = [char for char in messy_str if char not in string.punctuation]
    clean_str = ''.join(clean_list)
    return clean_str


data['review'] = data['review'].apply(punctuation_removal)

# data['review'] = data['review'].apply(nfx.remove_currency_symbols)
# data['review'] = data['review'].apply(nfx.remove_stopwords)
# data['review'] = data['review'].apply(nfx.remove_numbers)
# data['review'] = data['review'].apply(nfx.remove_currencies)
# data['review'] = data['review'].apply(nfx.remove_bad_quotes)
# data['review'] = data['review'].apply(nfx.remove_special_characters)

data = data.drop_duplicates()


# train_sentiments = []
#
# for i in data['review']:
#     train_sentiments.append(id.polarity_scores(i).get('compound'))
#
# train_sentiments = np.asarray(train_sentiments)
# data['sentiment'] = pd.Series(data=train_sentiments)
#
#
# data = data.drop(['date','uniqueID','review','len'], axis=1)

# sentiment was removed from the above list

def main():
    st.title('IOU PROJECT by Abideen')
    st.subheader("Drug Prescription Model based on Review of users")

    if st.checkbox("Give drug review"):

        condition = st.text_input("Enter your medical condition: ")

        drug = st.text_input("What drug was described for you by a doctor?: ")

        text = st.text_input(f'What is your review on {drug}?')

        if st.button("Send Review"):
            sentiment = get_sentiment(text)
            review = f"Your review on {drug} for {condition} is {sentiment} "

            st.write(review)

  if st.checkbox("Get drug rating and prescription"):
    condition = data['condition'].unique().tolist()
        
    drug_picked = st.selectbox("Select conditions", condition)
    if st.button("get drug"):
        st.write("Top 5")
        top_drugs = data[data['condition'] == drug_picked].groupby('drugName')['usefulCount'].sum() \
                        .reset_index().sort_values(by='usefulCount', ascending=False).head()
        st.write(top_drugs, table=True)

        st.write("Bottom 5")
        bottom_drugs = data[data['condition'] == drug_picked].groupby('drugName')['usefulCount'].sum() \
                        .reset_index().sort_values(by='usefulCount', ascending=True).head()
        st.write(bottom_drugs, table=True)



st.sidebar.subheader("About the School")
st.sidebar.text('''The International Open University (IOU),previously known as the Islamic Online University, 
was launched by Dr. Bilal Philips in 2007 as a higher education institution that offers affordable online 
undergraduate and graduate programs.''')


if __name__ == '__main__':
    main()
