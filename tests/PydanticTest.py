from ToDoApp.core.utils import DataWork
from ToDoApp.core.schemas.task_schema import Task

task = None

filepath = "C:\\Users\\sultan\\PycharmProjects\\ToDoFastAPIProject\\ToDoApp\\core\\data\\schemas_tasks.json"
data = DataWork.get_json(filepath)
task = Task(name=task)
print(task.model_dump())
data.append(task.model_dump())
print(data)
DataWork.change_json(data, filepath)

