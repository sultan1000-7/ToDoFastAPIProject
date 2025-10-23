import logging
from time import sleep

import asyncio
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, delete, update

from ToDoApp.core.models.task_model import Tasks
from ToDoApp.dababase.db_helper import db
from ToDoApp.core.schemas.task_schema import Task

path_to_logging = "C:\\Users\\sultan\\PycharmProjects\\ToDoFastAPIProject\\log\\py_log.log"

logging.basicConfig(level=logging.DEBUG, filename=path_to_logging, filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


async def get_all_tasks():
    async with db.session() as session:
        result = await session.scalars(select(Tasks))
        tasks = result.all()
        logging.debug(tasks)

        if result is None:
            raise SQLAlchemyError("В таблице нет полей")

        return __db_to_list(tasks)



async def get_task(task_id: int):
    async with db.session() as session:
        result = await session.scalar(select(Tasks).where(Tasks.id == task_id))

        if result is None:
            raise SQLAlchemyError("This id does not exist")

        return {"id": result.id, "title": result.title}


async def add_task(task: Task):
    async with db.session() as session:
        if task is not None:
            new_task = Tasks(title=task.title)
            session.add(new_task)
            await session.commit()
            await session.refresh(new_task)
            return {"id": new_task.id, "title": new_task.title}

        return None




async def delete_task(task_id: int):
    async with db.session() as session:
        task = await session.scalar(select(Tasks).where(Tasks.id == task_id))

        if task is None:
            return None

        await session.delete(task)
        await session.commit()

        return {"id": task.id, "title": task.title}


async def update_task(task_id: int, new_task: str):
    async with db.session() as session:
        if new_task is not None:
            task = await session.scalar(select(Tasks).where(Tasks.id == task_id))

            if task is None:
                return None

            task.title = new_task
            await session.commit()
            await session.refresh(task)

            return {"id": task.id, "title": task.title}

        return None


async def is_id(task_id: int) -> bool:
    async with db.session() as session:
        result = await session.scalar(select(Tasks).where(Tasks.id == task_id))

        if result is not None:
            return True

        return False


def __db_to_list(tasks) -> list:
    result = []
    for task in tasks:
        result.append({"id": task.id, "title": task.title})

    return result
