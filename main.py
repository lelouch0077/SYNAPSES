from fastapi import FastAPI, Query
from db import get_products
from search import smart_search

app = FastAPI()

@app.get("/search")
def search(q: str = Query(...), category: str = None):
    results = smart_search(q, category)
    return {"results": results}

@app.get("/products")
def get_all_products():
    return get_products()
