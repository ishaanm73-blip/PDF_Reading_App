import streamlit as st
import requests
BACKEND_URL = "http://127.0.0.1:8000/api"
st.title("PDF READER APP")
st.write("Upload PDF file and get answers to questions about it")

# FILE UPLOAD PART
st.header("Upload a pdf file")
pdf = st.file_uploader("Choose a file",type=["pdf"])
if pdf is not None:
    files = {"file": (pdf.name,pdf,"application/pdf")}
    response = requests.post(f"{BACKEND_URL}/upload",files=files)
    if response.status_code==200:
        st.success(f"File uploaded! Chunks created! {response.json()['chunks']}")
    else:
        st.error("File coudnt be uploaded!")

#QUESTION ANSWERED PART
st.header("Ask a question")
question = st.text_input("Your question")

if st.button("Ask"):
    if not question.strip():
        st.error("Please ask a question")
    else:
        params = {"question":question}
        response = requests.get(f"{BACKEND_URL}/ask",params=params)
        if response.status_code==200:
            data = response.json()
            st.subheader("Answer")
            st.write(data["answer"])
            with st.expander("Retrieved Context"):
                st.write(data["context"])
        else:
            st.error("Query failed!")