import logging

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, delete, update

from ..models.task_model import Tasks
from ...dababase.db_helper import db
from ..schemas.task_schema import Task
from ..utils import DataWork

path_to_logging = "C:\\Users\\sultan\\PycharmProjects\\ToDoFastAPIProject\\log\\py_log.log"

logging.basicConfig(level=logging.DEBUG, filename=path_to_logging, filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


def get_all_tasks():
    result = db.session.scalars(select(Tasks))
    logging.debug(result)

    if result is not None:
        return __db_to_list(result)
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

        return new_task

    return None


def delete_task(task_id: int):
    if task_id is not None:
        task = db.session.scalar(select(Tasks).where(Tasks.id == task_id))

        logging.debug(task)

        if task is None:
            return task

        # db.session.delete(db.session.scalar(select(Tasks).where(Tasks.id == task_id)))
        db.session.query(Tasks).filter(Tasks.id == task_id).delete()
        db.session.commit()

        return task

    return None


def update_task(task_id: int, new_task: str):
    if task_id is not None and new_task is not None:
        db.session.query(Tasks).filter(Tasks.id == task_id).update({"title": new_task})
        db.session.commit()
        return new_task

    return None


def is_id(task_id: int):
    result = db.session.scalar(select(Tasks).where(Tasks.id == task_id))

    if result is not None:
        return True

    return False


def __db_to_list(tasks):
    result = []
    for task in tasks:
        result.append({"id": task.id, "title": task.title})

    return result
