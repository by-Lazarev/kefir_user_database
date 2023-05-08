from pydantic import BaseModel
from datetime import date


class UserBase(BaseModel):
    class Config:
        orm_mode = True


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
    email: str
    phone: str
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
    second_name: str
    other_name: str
    email: str
    phone: str
    city: int
    additional_info: str
    is_admin: bool
    password: str


class PrivateDetailUserResponseModel(UserBase):
    id: int
    first_name: str
    second_name: str
    other_name: str
    email: str
    phone: str
    city: int
    additional_info: str
    is_admin: bool


class PrivateUpdateUserModel(UserBase):
    id: int
    first_name: str
    second_name: str
    other_name: str
    email: str
    phone: str
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
    email: str


class PrivateUsersListResponseModel(UserBase):
    data: UsersListElementModel
    meta: PrivateUsersListMetaDataModel


class UpdateUserModel(UserBase):
    first_name: str
    last_name: str
    other_name: str
    email: str
    phone: str
    birthday: date


class UpdateUserResponseModel(UserBase):
    id: int
    first_name: str
    last_name: str
    other_name: str
    email: str
    phone: str
    birthday: date


class UsersListMetaDataModel(UserBase):
    pagination: PaginatedMetaDataModel


class UsersListResponseModel(UserBase):
    date: UsersListElementModel
    meta: UsersListMetaDataModel
