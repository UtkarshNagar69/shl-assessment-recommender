import json
import faiss
import numpy as np
from app.embedder import embed_texts, embed_query

with open("app/data/shl_catalog.json") as f:
    data = json.load(f)

descriptions = [item["description"] for item in data]
embeddings = embed_texts(descriptions)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def recommend(query, top_k=5):
    query_vec = embed_query(query)
    D, I = index.search(np.array(query_vec), top_k)
    return [data[i] for i in I[0]]
