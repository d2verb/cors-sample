from typing import Optional
from fastapi import FastAPI, Response, Header

app = FastAPI()

@app.get("/me")
def me(response: Response, origin: Optional[str] = Header(None)):
    response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:8001"
    return {
        "name": "john",
        "about": "I want to be a shellfish.",
        "homepage": "https://shellfi.sh"
    }
