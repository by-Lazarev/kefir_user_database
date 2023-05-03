from fastapi import APIRouter

router = APIRouter(
    prefix="/private",
    tags=["admin"]
)


@router.get(
    "/users",
    summary="Постраничное получение кратких данных обо всех пользователях",
    description="Здесь находится вся информация, доступная пользователю о других пользователях"
)
def get_all_users():
    return {"msg": "OK"}


@router.post(
    "/users",
    summary="Создание пользователя",
    description="Здесь возможно занести в базу нового пользователя с минимальной информацией о нем"
)
def add_user():
    return {"msg": "OK"}


@router.get(
    "/users/{user_id}",
    summary="Детальное получение информации о пользователе",
    description="Здесь администратор может увидеть всю существующую пользовательскую информацию"
)
def get_user_by_id():
    return {"msg": "OK"}


@router.delete(
    "/users/{user_id}",
    summary="Удаление пользователя",
    description="Удаление пользователя"
)
def delete_user_by_id():
    return {"msg": "OK"}


@router.patch(
    "/users/{user_id}",
    summary="Изменение информации о пользователе",
    description="Здесь администратор может изменить любую информацию о пользователе"
)
def update_user_by_id():
    return {"msg": "OK"}
