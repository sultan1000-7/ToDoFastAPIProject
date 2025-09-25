from ToDoApp.core.utils import DataWork
from ToDoApp.core.schemas.task_schema import Task
from ToDoApp.dababase.db_helper import *
from ToDoApp.core.models.task_model import Tasks

from sqlalchemy import select


def add_task(title: str):
    new_task = Tasks(title=title)

    db.session.add(new_task)
    db.session.commit()

def display_tasks():
    statement = select(Tasks)
    result = db.session.scalars(statement)

    for field in result:
        print(f"{field.id} - {field.title}")

display_tasks()