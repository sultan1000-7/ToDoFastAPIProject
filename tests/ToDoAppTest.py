from ToDoApp.core.utils import DataWork

import os

filepath = os.path.abspath('../') + "\\ToDoFastAPIProject\\ToDoApp\\core\\data\\tasks.json"

print(DataWork.get_next_id(filepath))



