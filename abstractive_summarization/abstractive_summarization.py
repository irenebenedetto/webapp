import streamlit as st
from transformers import BartForConditionalGeneration
from transformers import BartTokenizer

# TO-DO gestire cache

def app():

    st.title('Abstractive summarization')
    st.write('Abstractive summarization is the task that aims to generate a novel text that summarizes the content of a long input text. Enter a long text in the area below and summarize it. You can also select the minimum and maximum number of words for the summary.')

    exp = st.expander('Parameters for abstractive summarization')
    exp.write('Select the minimum and the maximum size of the summary to generate')
    values = exp.slider(' ', 30, 250, (50, 150))

    default_text = """
    The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.
    """.strip()
    text_to_summarize = st.text_area('Enter a text to summarize', default_text, height=300)
    if st.button('Summarize') and values:
        model_path = './abstractive_summarization/checkpoints/model'
        tokenizer_path = './abstractive_summarization/checkpoints/tokenizer'
        model = BartForConditionalGeneration.from_pretrained(model_path)
        tokenizer = BartTokenizer.from_pretrained(tokenizer_path)

        inputs = tokenizer(text_to_summarize, truncation=True, max_length=1024, return_tensors='pt')

        summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=values[1], min_length=values[0])

        summary = ' '.join([tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids])
        st.subheader('Summary')
        st.write(summary)
