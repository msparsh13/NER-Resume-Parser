import streamlit as st
from PyPDF2 import PdfReader 
import spacy 
from spacy import displacy
from nltk.corpus import stopwords

nlp = spacy.load(r"C:\Users\Sparsh Mahajan\OneDrive\Documents\c progams\.vscode\.vscode\backend\NER-Resume Parser\model-best")

stop=set(stopwords.words('english'))


st.header("Resume Parser")


upload_file = st.file_uploader(label="Upload Your Resume in Pdf format", type="pdf")


if upload_file is not None:
    reader = PdfReader(upload_file) 
    text=""
    for i in range(len(reader.pages)):

        page = reader.pages[i]
        text += page.extract_text()

check = st.button(label="click")


if check and text :
    doc =nlp(text)
    ent = displacy.render(doc, style="ent", jupyter=False)
    st.markdown(ent, unsafe_allow_html=True)