from typing import Union

from fastapi import FastAPI
import led
app = FastAPI()


@app.get("/")
def read_root():
    led.led_on()
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None): # q可以是字符串或者None，如果不指定q，那么q就是None
    return {"item_id": item_id, "q": q}