# 📚 Document Search & Summarization with LLMs

This project builds a system that can **search across a large text corpus and generate concise summaries** of the most relevant documents using a Large Language Model (LLM).

---

## 🔍 What This Project Does

- Lets a user ask a **natural language query** (e.g., “What are the key benefits of renewable energy policies in Europe?”).
- Searches a prepared corpus using **traditional IR methods (TF‑IDF/BM25)** plus **LLM-based embeddings** for better relevance. 
- Returns the **top N relevant documents or passages** for that query. 
- Uses an LLM to **summarize those documents** into a coherent answer, with optional control over the summary length. 
---

## 🧱 Main Components

1. **Data Preparation**  
   - Load a sizable text corpus.  
   - Clean and pre-process it so it is ready for search and summarization (tokenization, normalization, indexing, embeddings, etc.). 

2. **Document Search**  
   - Ingest user queries and retrieve relevant documents from the corpus.  
   - Combine classic retrieval (e.g., TF‑IDF/BM25) with **embedding-based search** to improve accuracy. 

3. **Document Summarization**  
   - Feed the retrieved documents to an LLM (e.g., GPT‑4 or similar).  
   - Generate a **succinct, coherent summary** that captures the main ideas.  
   - Allow the user to specify a **short, medium, or long** summary length. 

4. **Evaluation**  
   - Build a small test set where each query has an intended “correct” document.  
   - Measure **search accuracy** (how often the right document is retrieved).  
   - Evaluate summaries using automatic metrics like **ROUGE** and human judgment. 

5. **User Interface**  
   - Provide a simple UI or API where users can type queries and view:  
     - Ranked search results.  
     - Generated summary.  
   - Nice-to-have features: query auto-suggestions, pagination, adjustable summary length.

---

## 🧪 Deliverables in This Project

- **Code** for:
  - Data preparation and indexing.  
  - Search and retrieval logic.  
  - LLM-based summarization.  
  - Evaluation scripts. 



