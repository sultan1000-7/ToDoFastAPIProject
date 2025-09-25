from sqlalchemy.orm import declarative_base, Mapped
from sqlalchemy import Column, Integer, String
from sqlalchemy.testing.schema import mapped_column

Base = declarative_base()

class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)

