from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError, HTTPException
from pydantic import ValidationError

from routers import admin, user
from test_app import errors_handling
from auth import auth
from db import models
from db.database import engine
from handlers import middleware

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

models.Base.metadata.create_all(engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_exception_handler(Exception, middleware.exception_handler)
app.add_exception_handler(RequestValidationError, middleware.validation_exception_handler)
app.add_exception_handler(ValidationError, middleware.validation_error_handler)
app.add_exception_handler(HTTPException, middleware.http_exception_handler)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(admin.router)
app.include_router(errors_handling.router)
