import pickle
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import TOP_K


with open("bm25.pkl", "rb") as f:
    bm25 = pickle.load(f)


with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Load FAISS with LOCAL embeddings (NO OpenAI)
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


vectorstore = FAISS.load_local(
            "faiss_index",
            embeddings,
            allow_dangerous_deserialization=True
        )
def hybrid_search(query, k=TOP_K):
    dense_docs = vectorstore.similarity_search(query, k=k)
    sparse_scores = bm25.get_scores(query.split())


    scores = {}
    for d in dense_docs:
        scores[d.page_content] = scores.get(d.page_content, 0) + 0.6


    for i, score in enumerate(sparse_scores):
        scores[chunks[i]["text"]] = scores.get(chunks[i]["text"], 0) + 0.4 * score


    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [r[0] for r in ranked[:k]]