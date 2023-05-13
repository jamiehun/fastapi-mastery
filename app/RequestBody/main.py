from fastapi import FastAPI
from pydantic import BaseModel 

class Item(BaseModel):
    name: str 
    description: str | None = None 
    price: float 
    tax: float | None = None 
    
app = FastAPI() 

# 1. Request Body Only 
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax 
        item_dict.update({"price_with_tax" : price_with_tax})
    return item_dict

# 2. Request Body + Path Parameters 
# if the uri is same as the #3, the Swagger UI won't show this info.
@app.put("/item/{item_id}")
async def create_item2(item_id: int, item: Item):
    return {"item_id" : item_id, **item.dict()}

# 3. Request Body + Path Parameters + Query Parameters 
@app.put("/items/{item_id}")
async def create_item3(item_id: int, item: Item, q: str | None = None):
    result = {"item_id" : item_id, **item.dict()}
    if q:
        result.update({"q" : q})
    return result 