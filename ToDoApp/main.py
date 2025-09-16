import os.path

from fastapi import FastAPI
from ToDoApp.core.utils import DataWork

app = FastAPI()

filepath = os.path.abspath("core/data/tasks.json")


@app.get("/")
async def root():
    return {"message": f"Hello World DEV_MODE"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name} "}


@app.get("/ToDo")
def get_ToDo():
    return DataWork.get_json(filepath)