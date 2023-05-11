from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status

from db import schemas
from db.models import DbUser


def create_user(request: schemas.PrivateCreateUserModel, db: Session):
    new_user = DbUser(
        first_name=request.first_name,
        last_name=request.last_name,
        other_name=request.other_name,
        email=request.email,
        phone=request.phone,
        city=request.city,
        additional_info=request.additional_info,
        is_admin=request.is_admin,
        password=request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def read_all_users(db: Session):
    return db.query(DbUser).all()


def read_user_by_id(db: Session, user_id: int):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found")
    return user


def update_user_by_id(db: Session, user_id: int, request: schemas.PrivateUpdateUserModel):
    user = db.query(DbUser).filter(DbUser.id == user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found")

    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: request.password
    })
    db.commit()
    return read_user_by_id(db, user.id)  # TODO: need to check whether the req. params is NULL


def delete_user(db: Session, user_id: int):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found")
    db.delete(user)
    db.commit()
    return "OK"
