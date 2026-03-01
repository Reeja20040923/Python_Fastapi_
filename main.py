from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message":"Hello! Welcome to FastAPI!"}

@app.get("/greet")
def greet():
    return {"Message": "Hello ! Reeja"}

@app.get("/greet/{name}")
def greet_name(name:str, age:Optional[int]=None):
    return {"Message":f"hello!{name}, you are {age} years old"}