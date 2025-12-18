import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from retrieval.hybrid_search import hybrid_search
from summarization.summarizer import summarize


st.title("📄 Document Search & Summarization (RAG)")


query = st.text_input("Enter your query")
length = st.slider("Summary length", 50, 300, 150)


if st.button("Search & Summarize"):
    docs = hybrid_search(query)
    summary = summarize(docs, length)
    st.subheader("Summary")
    st.write(summary)