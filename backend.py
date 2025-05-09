from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # 모델 선언

class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price : float

@app.get("/")
async def read_root():
    return "This is root path from MyAPI"

@app.get("/items/{item_id}")
async def read_item(item_id : int, q: Optional[str] = None):
    return {"item_id" : item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    result = {"item_id": item_id, **item.dict()}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}