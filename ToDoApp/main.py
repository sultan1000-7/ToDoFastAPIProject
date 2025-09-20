import os.path
import logging

import uvicorn
from fastapi import FastAPI
from typing import Optional

from ToDoApp.core.utils import DataWork
from ToDoApp.core.schemas.task_schema import Task

app = FastAPI()

filepath = os.path.abspath("../") + "\\ToDoFastAPIProject\\ToDoApp\\core\\data\\tasks.json"
schemas_filepath = os.path.abspath("../") + "\\ToDoFastAPIProject\\ToDoApp\\core\\data\\schemas_tasks.json"
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

@app.get("/ToDo/schemas")
def get_todo():
    return DataWork.get_json(schemas_filepath)


@app.get("/ToDo/{id_todo}")
def get_todo_by_id(id_todo: int):
    data = DataWork.get_json(filepath)
    for task in data:
        if task["id"] == id_todo:
            return task


@app.get("/ToDo/schemas/{id_todo}")
def get_todo_by_id(id_todo: int):
    data = DataWork.get_json(schemas_filepath)
    for task in data:
        if task["id"] == id_todo:
            return task


@app.get('/ToDo/add/task')
def add_task(new_task: Optional[str]):
    next_id = DataWork.get_next_id(filepath)
    if new_task is None:
        logging.error(f"/ToDo/add/task incorrect variable values: {new_task}")
        return {"status": "error", "message": "incorrect variable values"}
    if next_id == -1 and next_id == 0:
        logging.error(f"/ToDo/add/task error kin task id: {next_id}")
        return {"status": "error", "message": "error in task id"}
    else:
        data = DataWork.get_json(filepath)
        data.append({"id": next_id, "task": new_task})
        DataWork.change_json(data, filepath)
        return {"status": "ok"}


@app.get("/ToDo/add/schemas/task")
def add_task_from_schemas(new_task: Optional[str]):
    try:
        task = Task(name=new_task)
        logging.debug(task.model_dump_json())
        data = DataWork.get_json(schemas_filepath)
        data.append(task)
        DataWork.change_json(data, schemas_filepath)
    except ValueError as e:
        return {"status": "error", "message": f"{e}"}


@app.get('/ToDo/delete/task/{id_todo}')
def delete_task_by_id(id_todo: int):
    tasks = DataWork.get_json(filepath)
    i = 0
    is_delete = False
    while i < len(tasks) and not is_delete:
        task = tasks[i]
        if task["id"] == id_todo:
            tasks.remove(task)
            is_delete = True
        i += 1

    if is_delete:
        DataWork.change_json(tasks, filepath)

        return {"status": "ok"}

    return {"status": "error", "message": f"{id_todo} id already exists"}


@app.get("/ToDo/update/task")
def update_task_by_id(id_todo: int, new_task: str):
    tasks = DataWork.get_json(filepath)
    i = 0
    is_update = False
    while i < len(tasks) and not is_update:
        task = tasks[i]
        if task["id"] == id_todo:
            task["task"] = new_task
            is_update = True
        i += 1
    if is_update:
        DataWork.change_json(tasks, filepath)

        return {"status": "ok"}

    return {"status": "error", "message": f"id {id_todo} not found"}


if __name__ == "__main__":
    uvicorn.run("ToDoApp.main:app", reload=True)
