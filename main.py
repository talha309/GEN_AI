from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional

# FastAPI app instance
app = FastAPI()

# Basic GET endpoint
@app.get("/person")
def get_person():
    return {"message": "Welcome to FastAPI"}

# Path parameter in FastAPI
@app.get("/person/{person_id}")
def get_person1(person_id: int):
    return {"status": "ok", "person_id": person_id}

# Query parameter in FastAPI
@app.post("/search")
def put_person(q: Optional[str] = Query(None, description="Query string")):
    return {"status": "ok", "query": q}

# Body parameter in FastAPI
class Person(BaseModel):
    person_id: int
    name: str
    age: int
    email: str

@app.post("/person")
def post_data(person: Person):
    return {
        "person_id": person.person_id,
        "person_name": person.name,
        "person_age": person.age,
        "person_email": person.email
    }