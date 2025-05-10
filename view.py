import streamlit as st

st.set_page_config(page_title="RAG Demo", page_icon=":guardsman:", layout="wide")
st.title("RAG Demo with LangChain and DeepSeek")
st.write("This is a demo of a Retrieval-Augmented Generation (RAG) system using LangChain and DeepSeek.")
st.sidebar.title("User Input")
st.sidebar.write("Enter your question below:")
user_question = st.sidebar.text_input("Question", "京剧旦角主要分为哪几个流派？")
st.sidebar.write("Select the number of documents to retrieve:")
num_docs = st.sidebar.slider("Number of documents", min_value=1, max_value=10, value=5)
t = st.sidebar.slider("t", min_value=1, max_value=10, value=1)
st.write(f"## {num_docs} documents will be retrieved for the question: {user_question}")
