from fastapi import FastAPI

app = FastAPI()

@app.get("/me")
def me():
    return {
        "name": "john",
        "about": "I want to be a shellfish.",
        "homepage": "https://shellfi.sh"
    }
