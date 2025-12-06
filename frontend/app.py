import streamlit as st
import requests
BACKEND_URL = "http://127.0.0.1:8000/api"
st.title("PDF READER APP")
st.write("Upload PDF file and get answers to questions about it")

st.header("Upload a pdf file")
pdf = st.file_uploader("Choose a file",type=["pdf"])
if pdf is not None:
    files = {"file": (pdf.name,pdf,"applications/pdf")}
    response = requests.post(f"{BACKEND_URL}/upload",files=files)
    if response.status_code==200:
        st.success(f"File uploaded! Chunks created! {response.json()['chunks']}")
    else:
        st.error("File coudnt be uploaded!")