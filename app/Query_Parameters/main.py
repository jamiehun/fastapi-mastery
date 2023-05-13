# When you declare other function parameters that are not part of the 
# path parameters, they are automatically interpreted as "query" parameters.

from fastapi import FastAPI 

app = FastAPI()

fake_item_db = [{"item_name" : "Foo"}, {"item_name" : "Bar"}, {"item_name" : "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_item_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item2(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q" : q})
    if not short:
        item.update(
            {"description" : "This is an amazing item that has a long description"}
        )
    return item 