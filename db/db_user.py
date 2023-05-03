from sqlalchemy.orm.session import Session

from db.schemas import PrivateCreateUserModel
from db.models import DbUser


def create_user(request: PrivateCreateUserModel, db: Session):
    new_user = DbUser(
        first_name=request.first_name,
        second_name=request.second_name,
        is_admin=request.is_admin
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
