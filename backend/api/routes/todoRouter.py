from api.model.User import User
from fastapi import APIRouter

todo_router = APIRouter(prefix="/api", tags=["Todo"])

@todo_router.get("/list")
def all_todos() -> str:
    return "Todos"

@todo_router.post("/create")
def create_todo(inputs: User) -> str:
    return inputs.name

@todo_router.put("/update/{key}")
def update_todo(key: int):
    return {"message": f"Todo with key {key} updated"}

@todo_router.delete("/delete/{key}")
def delete_todo(key: int):
    return {"message": f"Todo with key {key} deleted"}