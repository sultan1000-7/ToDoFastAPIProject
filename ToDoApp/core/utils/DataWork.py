import os
import json
import logging
from json import JSONDecodeError

from ToDoApp.core.schemas.task_schema import Task




filepath_for_logging = "C:\\Users\\sultan\\PycharmProjects\\ToDoFastAPIProject\\log\\py_log.log"

logging.basicConfig(level=logging.DEBUG, filename=filepath_for_logging, filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


def get_json(path_to_file: str):
    try:
        myjson = json.load(open(path_to_file, 'r'))
        return myjson
    except JSONDecodeError as e:
        logging.error(e)
        return []



def change_json(arr: list, path_to_file: str):
    if arr is not None and len(arr) > 0:
        with open(path_to_file, 'w') as file:
            arr = __sort_json(arr)
            file.write(json.dumps(arr))


def get_next_id(filepath : str):
    # tasks = get_json(filepath)
    #
    # result_id = tasks[len(tasks) - 1]["id"] + 1
    # return result_id


    tasks = get_json(filepath)
    result_id = 0

    if len(tasks) == 0:
        return 1
    elif len(tasks) > 1:
        last_id = 1
        i = 0
        while result_id == 0 and i < len(tasks):
            task = tasks[i]
            if task["id"] is not None:
                if task["id"] == 2 and i == 0:
                    result_id = 1
                if task["id"] != 1 and task["id"] - 1 != last_id:
                    result_id = last_id + 1
                elif task["id"] != 1 and task["id"] - 1 == last_id and i == len(tasks) - 1:
                    result_id = task["id"] + 1
                last_id = task["id"]
            i += 1
        if result_id == 0:
            result_id = -1
    else:
        task_id = tasks[0]["id"]
        if task_id > 1:
            result_id = task_id - 1
        elif task_id == 1:
            result_id = 2



    return result_id


def __sort_json(tasks: list):
    tasks = sorted(tasks, key=lambda d: d["id"])

    return tasks


