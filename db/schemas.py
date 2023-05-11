from pydantic import BaseModel, EmailStr, validator, constr
from datetime import date
from re import search, I


class UserBase(BaseModel):

    class Config:
        orm_mode = True
        use_enum_values = True


class ErrorResponseModel(BaseModel):
    code: int
    message: str


class CodelessErrorResponseModel(BaseModel):
    message: str = "Что-то пошло не так, мы уже исправляем эту ошибку"


class CitiesHintModel(UserBase):
    id: int
    name: str


class CurrentUserResponseModel(UserBase):
    first_name: str
    last_name: str
    other_name: str
    email: EmailStr
    phone: constr(
        regex=r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$",
        strip_whitespace=True,
        min_length=11
    )
    birthday: date
    is_admin: bool


class LoginModel(UserBase):
    login: str
    password: str


class PaginatedMetaDataModel(UserBase):
    total: int
    page: int
    size: int


class PrivateCreateUserModel(UserBase):
    first_name: str
    last_name: str
    other_name: str
    email: EmailStr
    phone: constr(
        regex=r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$",
        strip_whitespace=True,
        min_length=11
    )
    city: int
    additional_info: str
    is_admin: bool
    password: str


class PrivateDetailUserResponseModel(UserBase):
    id: int
    first_name: str
    last_name: str
    other_name: str
    email: EmailStr
    phone: constr(
        regex=r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$",
        strip_whitespace=True,
        min_length=11
    )
    city: int
    additional_info: str
    is_admin: bool


class PrivateUpdateUserModel(UserBase):
    id: int
    first_name: str
    last_name: str
    other_name: str
    email: EmailStr
    phone: constr(
        regex=r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$",
        strip_whitespace=True,
        min_length=11
    )
    city: int
    additional_info: str
    is_admin: bool


class PrivateUsersListHintMetaModel(UserBase):
    city: list[CitiesHintModel]


class PrivateUsersListMetaDataModel(UserBase):
    pagination: PaginatedMetaDataModel
    hint: PrivateUsersListHintMetaModel


class UsersListElementModel(UserBase):
    id: int
    first_name: str
    last_name: str
    email: EmailStr


class PrivateUsersListResponseModel(UserBase):
    data: list[UsersListElementModel]
    meta: PrivateUsersListMetaDataModel


class UpdateUserModel(UserBase):
    first_name: str
    last_name: str
    other_name: str
    email: EmailStr
    phone: constr(
        regex=r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$",
        strip_whitespace=True,
        min_length=11
    )
    birthday: date


class UpdateUserResponseModel(UserBase):
    id: int
    first_name: str
    last_name: str
    other_name: str
    email: EmailStr
    phone: constr(
        regex=r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$",
        strip_whitespace=True,
        min_length=11
    )
    birthday: date


class UsersListMetaDataModel(UserBase):
    pagination: PaginatedMetaDataModel


class UsersListResponseModel(UserBase):
    data: list[UsersListElementModel]
    meta: UsersListMetaDataModel
