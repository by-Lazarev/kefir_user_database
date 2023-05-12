from fastapi import APIRouter, Response, Depends, HTTPException, status
from sqlalchemy.orm.session import Session


from db.database import get_db
from db import schemas
from db.models import DbUser

router = APIRouter(
    tags=["auth"]
)


@router.post(
    "/login",
    summary="Вход в систему",
    description="После успешного входа в систему необходимо установить Cookies для пользователя",
    response_model=schemas.CurrentUserResponseModel
)
def login(request: schemas.LoginModel, db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.email == request.login).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if user.password != request.password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect name or password")

    return {"msg": "OK"}


@router.get(
    "/login",
    summary="Выход из системы",
    description="При успешном выходе необходимо удалить установленные Cookies"
)
def login():
    return {"msg": "OK"}
