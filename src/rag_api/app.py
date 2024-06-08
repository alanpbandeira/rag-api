from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def rag_call():
    return '<h1> Hello from rag on docker </h1>'

@app.get('/items/{item_id}')
async def read_items(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
