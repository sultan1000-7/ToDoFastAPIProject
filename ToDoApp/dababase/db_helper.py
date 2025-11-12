from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import Session



class DatabaseHelper:
    def __init__(self, url: str):
        self.__engine = create_async_engine(url=url)

        self.session = async_sessionmaker(self.__engine, expire_on_commit=False)




db = DatabaseHelper("postgresql+asyncpg://fastapi:fastapi123@localhost:5432/ToDo")
