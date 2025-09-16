import json


def get_json(path_to_file: str):
    with open(path_to_file, 'r') as file:
        return json.load(file)



def change_json(arr: list, path_to_file: str):
    with open(path_to_file, 'w') as file:
        file.write(json.dumps(arr))


