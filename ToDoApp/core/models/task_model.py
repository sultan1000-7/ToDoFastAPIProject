from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

from .base_model import Base



class Tasks(Base):
    __tablename__ = 'tasks'
    title: Mapped[str] = mapped_column(String(50))

    @property
    def dict(self):
        return {'id': self.id, 'title': self.title}

