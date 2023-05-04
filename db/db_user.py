from sqlalchemy.orm.session import Session

from db.schemas import PrivateCreateUserModel
from db.models import DbUser


def create_user(request: PrivateCreateUserModel, db: Session):
    new_user = DbUser(
        first_name=request.first_name,
        second_name=request.second_name,
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


def get_all_users(db: Session):
    return db.query(DbUser).all()


def get_user_by_id(db: Session, user_id: int):
    pass