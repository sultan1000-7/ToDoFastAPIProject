from ToDoApp.core.utils import DataWork

import os

filepath = os.path.abspath('../') + "\\ToDoFastAPIProject\\ToDoApp\\core\\data\\tasks.json"

result = DataWork.get_json(filepath)

print(result)

new_json = [{'id': 1, 'task': 'create ToDo list'}, {'id': 2, 'task': 'create ToDo list 2'}]

DataWork.change_json(new_json, filepath)

result = DataWork.get_json(filepath)

print(result)