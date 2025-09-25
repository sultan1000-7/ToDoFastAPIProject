from sqlalchemy import create_engine
from sqlalchemy.orm import Session



class DatabaseHelper:
    def __init__(self, url: str):
        self.__engine = create_engine(url)

        self.session = Session(self.__engine, future=True)




db = DatabaseHelper("postgresql://postgres:7SuLtAn13@localhost:5432/ToDo")
