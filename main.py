from fastapi import FastAPI, HTTPException
from fibo import fibo

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/fib/")
def get_fib(n: int):
    try:
        ret = fibo(n)
        return {"result": ret}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))