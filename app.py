from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()   ##fastapi object

@app.get("/")   ##decorator

def read_root():    ##auto converts dict into json
    return {"message": "Hello World"}

@app.get("/greet")

def greet_user(name: str):
    return{"message":f"hello {name}"}

class User(BaseModel):   ##pydantic model
    name:str
    age:int

@app.post("/user")
def create_user(user:User):
    return{
        "message": f"user {user.name} created.",
        "age":user.age
    }


   