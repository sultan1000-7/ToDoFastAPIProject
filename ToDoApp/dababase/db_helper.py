from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession



class DatabaseHelper:
    def __init__(self, url: str):
        self.__engine = create_async_engine(url=url, echo=True)

        self.session = async_sessionmaker(self.__engine, class_=AsyncSession ,expire_on_commit=False)


DATABASE_URL = "postgresql+asyncpg://fastapi:fastapi123@localhost:5432/ToDo"

db = DatabaseHelper(DATABASE_URL)
