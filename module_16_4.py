
from fastapi import FastAPI, Path, status, Body, HTTPException
from typing import Annotated, List
from pydantic import BaseModel


app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
def get_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
def create_user(user: User) -> str:
    users.append(user)
    user_id = len(users)
    return f'User {user_id} is registered'


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int):
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age

        return f'User {user_id} has been updated'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete('/user/{user_id}')
def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f'User {user_id} has been deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found!")