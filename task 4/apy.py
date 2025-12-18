from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Привет, это мой микросервис!"}

@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}

@app.get("/multiply")
def multiply_numbers(a: int, b: int):
    return {"result": a * b}