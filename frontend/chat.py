import streamlit as st
import requests
BACKEND_URL = "http://127.0.0.1:8000/api"
st.title("PDF Reader Chat Bot")
st.write("Upload a pdf file and chat with ai about its content")
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
#Creating chat history
if "messages" not in st.session_state:
    st.session_state["messages"]=[]
#Displaying messages
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**You** {msg['content']}")
    else:
        st.markdown(f"**assistant** {msg['content']}")
#User Input
user_input = st.chat_input("Ask a question")
#Handling user input
if user_input:
    st.session_state["messages"].append({"role":"user","content":user_input})
    history = [m["content"] for m in st.session_state["messages"]]
    response = requests.post(f"{BACKEND_URL}/ask",json={"question":user_input,"history":history})
    if response.status_code==200:
        answer = response.json()["answer"]
        st.session_state["messages"].append({"role":"assistant","content":answer})
        st.rerun()
    else:
        st.error("Backend Error Occurred")
                            