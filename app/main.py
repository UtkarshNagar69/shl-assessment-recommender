from fastapi import FastAPI
from app.recommend import recommend
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/api/recommend")
def get_recommendation(q: str):
    results = recommend(q, top_k=10)
    return {"results": results}