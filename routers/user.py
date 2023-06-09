from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db import schemas
from db import db_user
from db.database import get_db
from handlers import handlers

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
    return {"msg": "OK"}  # TODO: add method


@router.patch(
    "/current",
    summary="Изменение данных пользователя",
    description="Здесь пользователь имеет возможность изменить свои данные",
    response_model=schemas.PrivateUpdateUserModel
)
def update_user(request: schemas.UpdateUserModel):
    return {"msg": "OK"}  # TODO: add method


@router.get(
    "",
    summary="Постраничное получение кратких данных обо всех пользователях",
    description="Здесь находится вся информация, доступная пользователю о других пользователях",
    response_model=schemas.UsersListResponseModel
)
def read_current_user(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
    users_data = db_user.read_all_users(db)
    paginated_data = handlers.convert_to_pagination(users_data, page, size)
    return paginated_data
