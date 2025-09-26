import os.path
import logging

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from typing import Optional

from ToDoApp.core.utils import DataWork, DatabaseWork
from ToDoApp.core.schemas.task_schema import Task
from ToDoApp.core.models.task_model import Tasks
from ToDoApp.dababase.db_helper import db

app = FastAPI()

filepath = "C:\\Users\\sultan\\PycharmProjects\\ToDoFastAPIProject\\ToDoApp\\core\\data\\tasks.json"
schemas_filepath = "C:\\Users\\sultan\\PycharmProjects\\ToDoFastAPIProject\\ToDoApp\\core\\data\\schemas_tasks.json"
filepath_for_logging = "C:\\Users\\sultan\\PycharmProjects\\ToDoFastAPIProject\\log\\py_log.log"

logging.basicConfig(level=logging.DEBUG, filename=filepath_for_logging, filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


@app.get("/")
async def root():
    return {"message": f"Hello World DEV_MODE"}


@app.get("/docs")
def read_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json")


@app.get("/old/ToDo")
def get_todo():
    return DataWork.get_json(filepath)


@app.get("/ToDo")
def get_todo():
    return DataWork.get_json(schemas_filepath)


@app.get("/test/ToDo")
def get_todo():
    return DatabaseWork.get_all_tasks()


@app.get("/old/ToDo/{id_todo}")
def get_todo_by_id(id_todo: int):
    data = DataWork.get_json(filepath)
    for task in data:
        if task["id"] == id_todo:
            return task


@app.get("/ToDo/{id_todo}")
def get_todo_by_id(id_todo: int):
    data = DataWork.get_json(schemas_filepath)
    for task in data:
        if task["id"] == id_todo:
            return task


@app.get("/test/ToDo/{task_id}")
def get_todo_by_id(task_id: int):
    if DatabaseWork.is_id(task_id):
        task = DatabaseWork.get_task(task_id)
        if task.id == task_id:
            return task.__dict__
    else:
        return {"status": "error", "message": "there is no such id."}


@app.get('/old/ToDo/add/task')
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


@app.get("/ToDo/add/task")
def add_task_from_schemas(new_task: Optional[str]):
    try:
        task = Task()
        task.title = new_task
        data = DataWork.get_json(schemas_filepath)
        data.append(task.model_dump())
        DataWork.change_json(data, schemas_filepath)

        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": f"{e}"}


@app.get("/test/ToDo/add/task")
def add_task_from_schemas(new_task: Optional[str]):
    try:
        task = Task()
        task.title = new_task
        if task is not None:
            DatabaseWork.add_task(task)
            return {"status": "ok"}
        else:
            return {"status": "error", "message": "task not be None"}
    except Exception as e:
        return {"status": "error", "message": f"{e}"}


@app.get('/ToDo/delete/task/{id_todo}')
def delete_task_by_id_schemas(id_todo: int):
    tasks = DataWork.get_json(schemas_filepath)
    i = 0
    is_delete = False
    while i < len(tasks) and not is_delete:
        task = tasks[i]
        if task["id"] == id_todo:
            tasks.remove(task)
            is_delete = True
        i += 1

    if is_delete:
        DataWork.change_json(tasks, schemas_filepath)

        return {"status": "ok"}

    return {"status": "error", "message": f"{id_todo} id already exists"}


@app.get('/test/ToDo/delete/task/{task_id}')
def delete_task_by_id_schemas(task_id: int):
    task = DatabaseWork.delete_task(task_id)

    if task is not None:
        return {"status": "ok", "message": f"{task.title} is delete"}

    return {"status": "error", "message": "task not be exist"}


@app.get("/ToDo/update/task")
def update_task_by_id(id_todo: int, new_task: str):
    tasks = DataWork.get_json(schemas_filepath)
    i = 0
    is_update = False
    while i < len(tasks) and not is_update:
        task = tasks[i]
        if task["id"] == id_todo:
            task["name"] = new_task
            is_update = True
        i += 1
    if is_update:
        DataWork.change_json(tasks, schemas_filepath)

        return {"status": "ok"}

    return {"status": "error", "message": f"id {id_todo} not found"}

@app.get("/test/ToDo/update/task")
def update_task_by_id(task_id: int, new_task: str):
    result = DatabaseWork.update_task(task_id, new_task)

    if result is not None:
        return {"status": "ok"}

    return {"status": "error", "message": f"id {task_id} not found or title task value is empty"}


if __name__ == "__main__":
    uvicorn.run("ToDoApp.main:app")
