from fastapi import FastAPI, HTTPException
from models import Item
from database import add_item, delete_item, find_item, read_items, update_item

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the CRUD API"}

@app.get("/items/", response_model=list[Item])
def get_items():
    return read_items()

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = find_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    add_item(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item_endpoint(item_id: int, item: Item):
    updated = update_item(item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{item_id}", response_model=dict)
def delete_item_endpoint(item_id: int):
    deleted = delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
