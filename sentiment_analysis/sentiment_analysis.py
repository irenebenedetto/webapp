from transformers import pipeline
import streamlit as st
import gc

def app():
    gc.collect()
    st.title('Sentiment analysis')
    st.write("Analyse a small sentence and understand whether is positive, negative, or neutral.")

    default_text = """
        I really like the new design of your website!
        """.strip()
    text = st.text_area('Enter a text to analyze', default_text)

    button = st.button('Analyze the sentence')
    if button:
        gc.collect()
        sentiment_analysis = pipeline("sentiment-analysis", model="./sentiment_analysis/checkpoints/model/")
        sentiment = sentiment_analysis(text)[0]
        


        if sentiment['label'] == 'POSITIVE' or sentiment['label'] == 'LABEL_1':
            col1, col2 = st.columns((14, 1))
            col2.image('./sentiment_analysis/img/up.png')
            col1.subheader(f'Sentiment POSITIVE ({round(sentiment["score"] * 100, 2)}%)\n')
        elif sentiment['label'] == 'NEGATIVE' or sentiment['label'] == 'LABEL_0':
            col1, col2 = st.columns((14, 1))
            col2.image('./sentiment_analysis/img/down.png')
            col1.subheader(f'Sentiment NEGATIVE ({round(sentiment["score"] * 100, 2)}%)\n')
        else:
            col1, col2 = st.columns((14, 1))
            col2.image('./sentiment_analysis/img/neu.png')
            col1.subheader(f'Sentiment {sentiment["label"]} ({round(sentiment["score"] * 100, 2)}%)\n')
            
        gc.collect()

