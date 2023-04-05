from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel, Field


class ShopInfo(BaseModel):
    name: str
    location: str


class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]


class Data(BaseModel):
    x: int
    y: int


app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/hello")
async def index_2():
    return {"message": "Hello World2"}


@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}


@app.get("/countries2/")
async def country2(
    country_name: str = "japan", country_no: int = 1
):
    return {
        "country_name": country_name,
        "country_no": country_no,
    }


@app.get("/countries3/{country_name}")
async def country3(
    country_name: str = "japan", city_name: str = "tokyo"
):
    return {
        "country_name": country_name,
        "city_name": city_name,
    }


@app.get("/countries4/")
async def country4(
    country_name: Optional[str] = None,
    country_no: Optional[int] = None
):
    return {
        "country_name": country_name,
        "country_no": country_no,
    }


@app.post("/item/")
async def create_item(item: Item):
    return {"message": f"{item.name}は、税込価格{int(item.price*item.tax)}円です。"}


@app.post("/index/")
async def index2(data: Data):
    return {"data": data}


@app.get("/hello_data/")
def hello_data():
    return {"message": "Hello Deta!"}


@app.post("/hello_data/")
async def calc(data: Data):
    z = data.x*data.y
    return {"result": z}
