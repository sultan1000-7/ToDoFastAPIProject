from ToDoApp.dababase.db_helper import *
from ToDoApp.core.models.task_model import Tasks

from sqlalchemy import select
import asyncio


async def add_task(title: str):
    new_task = Tasks(title=title)

    await db.session.add(new_task)
    await db.session.commit()

async def get_tasks():
    statement = select(Tasks)
    tasks = await db.session.scalars(statement)

    result = []

    for field in tasks:
        result.append({"id" : field.id, "title" : field.title})

    return result


asyncio.run(get_tasks())
