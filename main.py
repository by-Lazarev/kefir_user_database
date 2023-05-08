from fastapi import FastAPI

from routers import admin, user
from auth import auth
from db import models
from db.database import engine

description = """
User Database provides API to CRUD user profiles.

## auth

* **login** - авторизация пользователя с использованием Cookies

## user

* **current** - получение/изменение данных текущего пользователя
* **users** - получение данных о всех пользователях

## admin

* **users** - получение/создание пользователей
* **{user_id}** - получение/изменение/удаление пользователя по его id
"""

tags_metadata = [
    {
        "name": "auth",
        "description": "Авторизация пользователей"
    },
    {
        "name": "user",
        "description": "Действия для авторизованных пользователей"
    },
    {
        "name": "admin",
        "description": "Действия для авторизованных администраторов"
    }
]

app = FastAPI(
    title="User Database",
    description=description,
    version="0.0.1",
    contact={
        "name": "Lazarev Nikita",
        "url": "https://t.me/lazanik",
        "email": "by.lazarev@gmail.com"
    },
    openapi_tags=tags_metadata
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(admin.router)

models.Base.metadata.create_all(engine)
