from ToDoApp.core.utils import DataWork
from ToDoApp.core.schemas.task_schema import Task
from ToDoApp.dababase.db_helper import *
from ToDoApp.core.models.task_model import Tasks

from sqlalchemy import select


def add_task(title: str):
    new_task = Tasks(title=title)

    db.session.add(new_task)
    db.session.commit()

def get_tasks():
    statement = select(Tasks)
    tasks = db.session.scalars(statement)

    result = []
    for field in tasks:
        result.append({"id" : field.id, "title" : field.title})

    return result

print(get_tasks())