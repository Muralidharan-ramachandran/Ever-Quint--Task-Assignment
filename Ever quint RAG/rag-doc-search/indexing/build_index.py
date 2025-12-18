from datasets import load_dataset
from indexing.chunking import chunk_documents
from indexing.embeddings import build_faiss
from indexing.bm25 import build_bm25
import pickle


print("Loading dataset...")
dataset = load_dataset("cnn_dailymail", "3.0.0", split="train[:100]")
documents = dataset["article"]


print("Chunking documents...")
chunks = chunk_documents(documents)


print("Building FAISS index...")
vectorstore = build_faiss(chunks)


print("Building BM25 index...")
bm25 = build_bm25(chunks)


with open("bm25.pkl", "wb") as f:
    pickle.dump(bm25, f)


with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("Indexing complete")