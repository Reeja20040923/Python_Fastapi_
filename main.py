from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

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

class Student(BaseModel):
    name: str
    age: int
    roll : int

@app.post("/student")
def create_student(student: Student):
    return{
    "name" : student.name,
    "age": student.age,
    "roll": student.roll
    }