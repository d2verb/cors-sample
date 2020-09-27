# CORS samples
## How to use
```
$ poetry install
$ poetry shell
$ cd 01_simple
$ uvicorn api:app --port=8000
$ uvicorn web:app --port=8001
```

## Patterns
1. simple request
2. with preflight request
3. with cookie
4. with api key
