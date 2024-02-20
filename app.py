from fastapi import FastAPI
from sqlalchemy import Column, INT, VARCHAR, create_engine
from sqlalchemy.orm import DeclarativeBase

from sqladmin import Admin, ModelView


engine = create_engine("sqlite:///db.sqlite3")


class Base(DeclarativeBase): ...


class Category(Base):
    __tablename__ = "categories"

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(length=32), nullable=False)

    def __str__(self) -> str:
        return self.name


Base.metadata.create_all(bind=engine)


class CategoryAdminView(ModelView, model=Category):
    icon = "fa-solid fa-list"
    name = "Категория"
    name_plural = "Категории"
    column_list = (Category.id, Category.name)
    column_searchable_list = (Category.name, )
    column_sortable_list = (Category.name, )


app = FastAPI()
admin = Admin(app=app, engine=engine)
admin.add_view(view=CategoryAdminView)

if __name__ == '__main__':
    from uvicorn import run
    run(app=app)
