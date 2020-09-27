from typing import Optional
from fastapi import FastAPI, Response, Header, Request

app = FastAPI()
api_key = "af0e1d8f3593d6b7f3e78ebf5b0898e6"

name_list = ["john", "joshua"]

profile = {
    "name": "john",
    "about": "I want to be a shellfish.",
    "homepage": "https://shellfi.sh"
}

@app.middleware("http")
async def authorize(request: Request, call_next):
    given_key = request.headers.get("Authorization", None)
    if given_key != api_key and request.method != "OPTIONS":
        return Response(status_code=403)
    response = await call_next(request)
    return response

@app.get("/me")
async def me(response: Response, origin: Optional[str] = Header(None)):
    response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:8001"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.set_cookie(key="hoge", value="fuga")
    return profile

@app.put("/me")
async def put(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:8001"

    global name_list
    name_list = name_list[1:] + name_list[:1]

    profile["name"] = name_list[0]
    return profile

@app.options("/me", status_code=204)
async def options(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:8001"
    response.headers["Access-Control-Allow-Headers"] = "Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET,PUT,OPTIONS"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Max-Age"] = "86400"
