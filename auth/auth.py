from fastapi import APIRouter

router = APIRouter(
    tags=["auth"]
)


@router.post(
    "/login",
    summary="Вход в систему",
    description="После успешного входа в систему необходимо установить Cookies для пользователя"
)
def login():
    return {"msg": "OK"}


@router.get(
    "/login",
    summary="Выход из системы",
    description="При успешном выходе необходимо удалить установленные Cookies"
)
def login():
    return {"msg": "OK"}
