import logging

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from typing import Optional

from ToDoApp.core.utils import DatabaseWork
from ToDoApp.core.schemas.task_schema import Task


app = FastAPI()

filepath = "C:\\Users\\sultan\\PycharmProjects\\ToDoFastAPIProject\\ToDoApp\\core\\data\\tasks.json"
schemas_filepath = "C:\\Users\\sultan\\PycharmProjects\\ToDoFastAPIProject\\ToDoApp\\core\\data\\schemas_tasks.json"
filepath_for_logging = "C:\\Users\\sultan\\PycharmProjects\\ToDoFastAPIProject\\log\\py_log.log"

logging.basicConfig(level=logging.DEBUG, filename=filepath_for_logging, filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


@app.get("/")
async def root():
    return {"message": f"Hello World"}


@app.get("/docs")
def read_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json")

@app.get("/todo")
def get_todo():
    return DatabaseWork.get_all_tasks()


@app.get("/todo/{task_id}")
def get_todo_by_id(task_id: int):
    if DatabaseWork.is_id(task_id):
        task = DatabaseWork.get_task(task_id)
        if task.id == task_id:
            return task.dict

        return {"status": "error", "message": "Task not found"}
    else:
        return {"status": "error", "message": "there is no such id."}



@app.get("/todo/add/task")
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



@app.get('/todo/delete/task/{task_id}')
def delete_task_by_id_schemas(task_id: int):
    task = DatabaseWork.delete_task(task_id)

    if task is not None:
        return {"status": "ok", "message": f"{task.title} is delete"}

    return {"status": "error", "message": "task not be exist"}


@app.get("/todo/update/task")
def update_task_by_id(task_id: int, new_task: str):
    result = DatabaseWork.update_task(task_id, new_task)

    if result is not None:
        return {"status": "ok"}

    return {"status": "error", "message": f"id {task_id} not found or title task value is empty"}


if __name__ == "__main__":
    uvicorn.run("ToDoApp.main:app")
