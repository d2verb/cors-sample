from typing import Optional
from fastapi import FastAPI, Response, Header

app = FastAPI()

name_list = ["john", "joshua"]

profile = {
    "name": "john",
    "about": "I want to be a shellfish.",
    "homepage": "https://shellfi.sh"
}

@app.get("/me")
def me(response: Response, origin: Optional[str] = Header(None)):
    response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:8001"
    response.set_cookie(key="hoge", value="fuga")
    return profile

@app.put("/me")
def put(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:8001"

    global name_list
    name_list = name_list[1:] + name_list[:1]

    profile["name"] = name_list[0]
    return profile

@app.options("/me", status_code=204)
def options(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:8001"
    response.headers["Access-Control-Allow-Methods"] = "PUT"
