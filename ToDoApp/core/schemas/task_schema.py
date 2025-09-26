from pydantic import BaseModel, Field, field_validator

from ..utils import DataWork


class Task(BaseModel):
    # id: int = Field(gt=0, default_factory=DataWork.get_next_id("C:\\Users\\sultan\\PycharmProjects\\ToDoFastAPIProject\\ToDoApp\\core\\data\\schemas_tasks.json"), description="Уникальный идентификатор задачи", alias="task_id")
    # name: str = Field(default="task", title="Название задачи", alias="task_name")
    id: int = Field(gt=0, default_factory=lambda: DataWork.get_next_id("C:\\Users\\sultan\\PycharmProjects\\ToDoFastAPIProject\\ToDoApp\\core\\data\\schemas_tasks.json"), description="Уникальный идентификатор задачи")
    title: str = Field(default="task", title="Название задачи", alias="task_title")

    @classmethod
    @field_validator("id", mode="before")
    def validate_id(cls, task_id):
        if task_id == -1 or task_id == 0:
            raise ValueError("Error generating the id")

        return task_id

    @classmethod
    @field_validator("title", mode="before")
    def validate_name(cls, title: str):
        if title is None:
            raise ValueError("incorrect variable values")

        return title