# My webapp

Source code for my [personal website](https://share.streamlit.io/irenebenedetto/webapp/main/main.py). 

This website shows four different demos:
- **Style transfer**: the goal of this task is to generate an image that has the style of a selected image (style-image) and the content of another one (content-image).
- **Abstractive summarization**: the aim of this task is to generate the abstractive summary of a long input text.
- **Sentiment analysis**: this task outputs the polarity of a sentence inserted, identifying if it is positive, negative or neutral.
- **Display your data**: insert a dataset (in CSV format) and select the feature to display with bar plot, line plot or map.


## Installation and usage

My personal website is available on-line at: https://share.streamlit.io/irenebenedetto/webapp/main/main.py. Unfortunately, the Stremalit Free plan limits the available resources to 1 GB and this may compromise the heaviest tasks, such as summarizaion and sentiment analysis. So, to run the code locally the following steps are required:
- Clone the repository;
```bash
git clone https://github.com/irenebenedetto/webapp.git
```
- Install the requirements from the requirements [file](https://github.com/irenebenedetto/webapp/blob/main/requirements.txt);
```bash
cd ./webapp
pip install -r ./requirements.txt
```
- Run locally with [Streamlit](https://streamlit.io);
```bash
streamlit run ./main.py
```
