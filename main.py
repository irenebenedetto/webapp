import streamlit as st
import base64
from multipage import *
from abstractive_summarization import abstractive_summarization
from style_transfer import style_transfer
#from image_captioning import image_captioning
from display_data import display_data
from about_me import about_me
from sentiment_analysis import sentiment_analysis
import gc




def create_main(sidebar=False):
    gc.collect()
    # Create an instance of the app
    app = MultiPage()

    # Add all your applications (pages) here
    app.add_page("Select an option", about_me.app)
    # app.add_page("Image captioning", image_captioning.app)
    app.add_page("Abstractive summarization", abstractive_summarization.app)
    app.add_page("Style transfer", style_transfer.app)
    app.add_page("Sentiment analysis", sentiment_analysis.app)
    app.add_page("Display your data", display_data.app)

    # The main app
    app.run(sidebar)

def run_app():
    gc.collect()
    st.markdown(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">',
        unsafe_allow_html=True)


    st.title('About me')

    st.sidebar.columns((1, 9))[1].image('./about_me/img/me.png', width=180)
    st.sidebar.columns((1, 9))[1].header('Irene Benedetto')

    _, col1, col2 = st.sidebar.columns((1, 1, 8))
    col1.markdown('<i class="fa fa-line-chart" style="font-size:24px"></i>', unsafe_allow_html=True)
    col2.write("Engineering and Management at [Politecnico di Torino](https://www.polito.it)")

    _, col1, col2 = st.sidebar.columns((1, 1, 8))
    col1.markdown('<i class="fa fa-sitemap" style="font-size:24px"></i>', unsafe_allow_html=True)
    col2.write("Data Science and Engineering at [Politecnico di Torino](https://www.polito.it)")


    _, col1, col2 = st.sidebar.columns((1, 1, 8))
    col1.markdown('<i class="fa fa-envelope" style="font-size:24px"></i>', unsafe_allow_html=True)
    col2.markdown("<p>ire <i>dot</i> benedetto <i>at</i> gmail <i>dot</i> com</p>", unsafe_allow_html=True)

    _, col1, col2 = st.sidebar.columns((1, 1, 8))
    col1.markdown('<i class="fa fa-map-marker" style="font-size:24px"></i>', unsafe_allow_html=True)
    col2.write("[Torino, Italy](https://goo.gl/maps/V57p9eojzmpFkkDe9)")

    _, col1 ,col2 = st.sidebar.columns((1, 1, 8))
    col1.markdown('<i class="fa fa-github" style="font-size:24px"></i>', unsafe_allow_html=True)
    col2.write("[GitHub](https://github.com/irenebenedetto)")

    _, col1, col2 = st.sidebar.columns((1, 1, 8))
    col1.markdown('<i class="fa fa-linkedin-square" style="font-size:24px;color:#2D6BC2"></i>', unsafe_allow_html=True)
    col2.write("[Linkedin](https://www.linkedin.com/in/irene-benedetto/)")



    st.write("""
    I am graduated in Data Science and Engineering at Politecnico di Torino. 
    Passionate about machine learning and deep learning, with particular interest in Natural Language Processing and Computer vision.
    """)

    pdf_file = './about_me/irene_benedetto_cv_word.pdf'
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        filename = 'cv-irene-benedetto'

        pdf_download = f'<p>For further information, see my <a href="data:application/octet-stream;base64,{base64_pdf}" download="{filename}.pdf">Curriculum Vitae</a>'


    st.markdown(pdf_download, unsafe_allow_html=True)

    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)

    col0, col1, col2 = st.columns((1, 8, 1))
    col0.markdown('<i class="fa fa-chevron-down" style="font-size:36px;text-align: center;"></i>', unsafe_allow_html=True)
    col1.markdown('<p style="font-size:20px;text-align:center"><b>Check out some experiments here</b></p>', unsafe_allow_html=True)
    col2.markdown('<i class="fa fa-chevron-down" style="font-size:36px;text-align: center;"></i>', unsafe_allow_html=True)
    create_main(sidebar=False)
    gc.collect()





if __name__ == "__main__":
    run_app()
