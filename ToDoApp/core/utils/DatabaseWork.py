from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from ..models.task_model import Tasks
from ...dababase.db_helper import db
from ..schemas.task_schema import Task



def get_all_tasks():
    result = db.session.scalar(select(Tasks))

    if result is not None:
        return result
    else:
        raise SQLAlchemyError("В таблице нет полей")


def get_task(task_id: int):
    result = db.session.scalar(select(Tasks).where(Tasks.id == task_id))

    if result is not None:
        return result
    else:
        raise SQLAlchemyError("Данного id не существует")


def add_task(task: Task):
    if task is not None:
        new_task = Tasks(title=task.title)
        db.session.add(new_task)
        db.session.commit()
        # Остановился здесь!!!


def is_id(task_id: int):
    result = db.session.scalar(select(Tasks).where(Tasks.id == task_id))

    if result is not None:
        return True

    return False
