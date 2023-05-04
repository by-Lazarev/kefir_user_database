from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db import schemas
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix="/private",
    tags=["admin"]
)


@router.get(
    "/users",
    summary="Постраничное получение кратких данных обо всех пользователях",
    description="Здесь находится вся информация, доступная пользователю о других пользователях"
)
def read_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


@router.post(
    "/users",
    summary="Создание пользователя",
    description="Здесь возможно занести в базу нового пользователя с минимальной информацией о нем",
    response_model=schemas.PrivateDetailUserResponseModel
)
def create_user(request: schemas.PrivateCreateUserModel, db: Session = Depends(get_db)):
    return db_user.create_user(request, db)


@router.get(
    "/users/{pk}",
    summary="Детальное получение информации о пользователе",
    description="Здесь администратор может увидеть всю существующую пользовательскую информацию"
)
def read_user_by_id(pk: int):
    return {"msg": "OK"}


@router.delete(
    "/users/{pk}",
    summary="Удаление пользователя",
    description="Удаление пользователя"
)
def delete_user_by_id(pk: int):
    return {"msg": "OK"}


@router.patch(
    "/users/{pk}",
    summary="Изменение информации о пользователе",
    description="Здесь администратор может изменить любую информацию о пользователе",
    response_model=schemas.PrivateUpdateUserModel
)
def update_user_by_id(pk: int, request: schemas.PrivateUpdateUserModel):
    return {"msg": "OK"}
