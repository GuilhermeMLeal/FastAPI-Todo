from fastapi import FastAPI
from api.routes.todoRouter import todo_router

app = FastAPI()
app.include_router(todo_router)

@app.get("/")
def read_root():
    return "Ola"
