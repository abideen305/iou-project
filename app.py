#!/usr/bin/env python
# coding: utf-8
import string

import pandas as pd
import streamlit as st


# import spacy


# def get_sentiment(text):
#     sentiment = SentimentIntensityAnalyzer().polarity_scores(text)
#     if sentiment['compound'] > 0:
#         return "Positive"
#     elif sentiment['compound'] == 0:
#         return "Neutral"
#     else:
#         return "Negative"


def sentiment_analysis(text):
    if "not" in text:
        return "Negative"
    elif "good" in text or "great" in text or "excellent" in text:
        return "Positive"
    else:
        return "Neutral"


# reading the Dataset
df = pd.read_csv('drug.csv')
data = df[['drugName', 'review', 'condition', 'usefulCount']]


# def punctuation_removal(messy_str):
#     clean_list = [char for char in messy_str if char not in string.punctuation]
#     clean_str = ''.join(clean_list)
#     return clean_str
#
#
# data['review'] = data['review'].apply(punctuation_removal)

# data['review']=data['review'].apply(nfx.remove_currency_symbols)
# data['review']=data['review'].apply(nfx.remove_stopwords)
# data['review']=data['review'].apply(nfx.remove_numbers)
# data['review']=data['review'].apply(nfx.remove_currencies)
# data['review']=data['review'].apply(nfx.remove_bad_quotes)
# data['review']=data['review'].apply(nfx.remove_special_characters)

# Clean data
# lets remove all the Duplicates from the Dataset
# data = data.drop_duplicates()


# train_sentiments = []

# for i in data['review']:
#     train_sentiments.append(sid.polarity_scores(i).get('compound'))

# train_sentiments = np.asarray(train_sentiments)
# data['sentiment'] = pd.Series(data=train_sentiments)


# lets remove the unique Id, date, review, len, and sentiment column also
# data = data.drop(['date','uniqueID','sentiment','review','len'], axis = 1)


def main():
    st.title('IOU PROJECT by Abideen')
    st.subheader("Natural Language project")

    if st.checkbox("Give drug review"):
        # text = input("Enter a text: ")

        text = st.text_input("Enter a text: ")
        sentiment = sentiment_analysis(text)
        if st.button("Review"):
            # sentiment = get_sentiment(text)
            st.success(sentiment)

            condition = st.text_input("Enter your medical condition: ")

            drug = st.text_input("What drug was described for you by a doctor?: ")

            review = st.text_input(f"What is your review on {drug}? ")
            #
            # text = "This is a great movie! I love it."
            # sentiment = TextBlob(text).sentiment

            st.write(review)
            # output Sentiment(polarity=0.8, subjectivity=0.75)
    # if st.checkbox("Get drug prescription"):
    #     st.selectbox("Pick a condition", list(data['condition'].unique()))
    #     if st.button("Get drug prescription"):
    #         st.success(sentiment)

    if st.checkbox("Get drug rating and prescription"):
        condition = list(data['condition'])
        drug_picked = st.selectbox("Select conditions", condition)
        if st.button("get drug"):
            st.write("Top 5")
            st.write(data[data['condition'] == drug_picked][['drugName', 'usefulCount']].sort_values
                     (by='usefulCount', ascending=False).head().reset_index(drop=True), table=True)
            st.write("Bottom 5")
            st.write(data[data['condition'] == drug_picked][['drugName', 'usefulCount']].sort_values
                     (by='usefulCount', ascending=True).head().reset_index(drop=True), table=True)


st.sidebar.subheader("About the project")
st.sidebar.text("IOU is an online university")
st.sidebar.button('click me')

if __name__ == '__main__':
    main()
