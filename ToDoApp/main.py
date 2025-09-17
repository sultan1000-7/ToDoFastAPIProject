import os.path
import logging

import uvicorn
from fastapi import FastAPI
from typing import Optional

from ToDoApp.core.utils import DataWork

app = FastAPI()

filepath = os.path.abspath("../") + "\\ToDoFastAPIProject\\ToDoApp\\core\\data\\tasks.json"
filepath_for_logging = os.path.abspath("../") + "\\ToDoFastAPIProject\\log\\py_log.log"

logging.basicConfig(level=logging.DEBUG, filename=filepath_for_logging, filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


@app.get("/")
async def root():
    return {"message": f"Hello World DEV_MODE"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/ToDo")
def get_todo():
    return DataWork.get_json(filepath)


@app.get("/ToDo/{id_todo}")
def get_todo_with_id(id_todo: int):
    data = DataWork.get_json(filepath)
    for task in data:
        if task["id"] == id_todo:
            return task

@app.get('/ToDo/add/task')
def post_task(new_task: Optional[str]):
    if new_task is None:
        logging.error(f"/ToDo/add/task incorrect variable values: {new_task}")
        return {"status" : "error" , "description" : "incorrect variable values"}
    else:
        data = DataWork.get_json(filepath)
        data.append({"id" : DataWork.get_next_id(filepath), "task" : new_task})
        DataWork.change_json(data, filepath)
        return {"status" : "ok"}


if __name__ == "__main__":
    uvicorn.run("ToDoApp.main:app", reload=True)
