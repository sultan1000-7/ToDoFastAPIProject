from pydantic import BaseModel, Field, field_validator



class Task(BaseModel):
    title: str = Field(default="task", title="Название задачи", alias="task_title")

    @classmethod
    @field_validator("title", mode="before")
    def validate_name(cls, title: str):
        if title is None:
            raise ValueError("incorrect variable values")

        return title
