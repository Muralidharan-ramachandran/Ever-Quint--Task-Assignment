from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def build_faiss(chunks):
    texts = [c["text"] for c in chunks]
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(texts, embeddings)
    vectorstore.save_local("faiss_index")
    return vectorstore