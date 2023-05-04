from fastapi import APIRouter

from db import schemas

router = APIRouter(
    tags=["auth"]
)


@router.post(
    "/login",
    summary="Вход в систему",
    description="После успешного входа в систему необходимо установить Cookies для пользователя",
    response_model=schemas.CurrentUserResponseModel
)
def login(request: schemas.LoginModel):
    return {"msg": "OK"}


@router.get(
    "/login",
    summary="Выход из системы",
    description="При успешном выходе необходимо удалить установленные Cookies"
)
def login():
    return {"msg": "OK"}
