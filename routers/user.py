from fastapi import APIRouter

from db import schemas

router = APIRouter(
    prefix="/users",
    tags=["user"]
)


@router.get(
    "/current",
    summary="Получение данных о текущем пользователе",
    description="Здесь находится вся информация, доступная пользователю о самом себе, а так же информация является ли "
                "он администратором",
    response_model=schemas.CurrentUserResponseModel
)
def read_current_user():
    return {"msg": "OK"}


@router.patch(
    "/current",
    summary="Изменение данных пользователя",
    description="Здесь пользователь имеет возможность изменить свои данные",
    response_model=schemas.PrivateUpdateUserModel
)
def update_user(request: schemas.UpdateUserModel):
    return {"msg": "OK"}


@router.get(
    "",
    summary="Постраничное получение кратких данных обо всех пользователях",
    description="Здесь находится вся информация, доступная пользователю о других пользователях",
    response_model=schemas.UsersListResponseModel
)
def read_current_user(page, size):  # Add query to control given nums
    return {"msg": "OK"}
