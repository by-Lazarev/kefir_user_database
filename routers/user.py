from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["user"]
)


@router.get(
    "/current",
    summary="Получение данных о текущем пользователе",
    description="Здесь находится вся информация, доступная пользователю о самом себе, а так же информация является ли "
                "он администратором"
)
def read_current_user():
    return {"msg": "OK"}


@router.patch(
    "/current",
    summary="Изменение данных пользователя",
    description="Здесь пользователь имеет возможность изменить свои данные"
)
def update_user():
    return {"msg": "OK"}


@router.get(
    "",
    summary="Постраничное получение кратких данных обо всех пользователях",
    description="Здесь находится вся информация, доступная пользователю о других пользователях"
)
def read_current_user():
    return {"msg": "OK"}
