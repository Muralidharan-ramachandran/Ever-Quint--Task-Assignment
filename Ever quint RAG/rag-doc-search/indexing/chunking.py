from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    all_chunks = []
    for doc_id, text in enumerate(documents):
        chunks = splitter.split_text(text)
        for idx, chunk in enumerate(chunks):
            all_chunks.append({
                "doc_id": doc_id,
                "chunk_id": f"{doc_id}_{idx}",
                "text": chunk
            })
    return all_chunks