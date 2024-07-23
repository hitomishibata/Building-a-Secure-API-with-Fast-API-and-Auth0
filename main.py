from enum import Enum
from typing import Annotated
from fastapi import FastAPI, Depends, Query, Security
from utils import VerifyToken


class CityName(str, Enum):
    Amsterdam = "amsterdam",
    The_Hague = "the_hague"
    Utrecht = "utrecht"


app = FastAPI()
auth = VerifyToken()

@app.get("/private")
def private(auth_result: str = Security(auth.verify)):
    return auth_result

@app.get("/private/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items":[{"item_id": 1}, {"item_id": 2 }]}
    if q:
        results.update({"q": q})
    return results

@app.get("/private/cities/{city_name}")
async def get_city(city_name: CityName):
    if city_name is CityName.Amsterdam:
        return {"city_name": city_name, "Average rent price of residential property in 2023 (in euros per square meter)": 25.68}
    
    if city_name is CityName.The_Hague:
        return  {"city_name": city_name, "Average rent price of residential property in 2023 (in euros per square meter)": 18.19}
    
    if city_name is CityName.Utrecht:
        return  {"city_name": city_name, "Average rent price of residential property in 2023 (in euros per square meter)": 19.83}
    
    return  {"city_name": city_name, "message": f"there is no data on {city_name} "}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

