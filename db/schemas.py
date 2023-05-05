from pydantic import BaseModel
from datetime import date


class ErrorResponseModel(BaseModel):
    code: int
    message: str


class CodelessErrorResponseModel(BaseModel):
    message: str = "Что-то пошло не так, мы уже исправляем эту ошибку"


class CitiesHintModel(BaseModel):
    id: int
    name: str


class CurrentUserResponseModel(BaseModel):
    first_name: str
    last_name: str
    other_name: str
    email: str
    phone: str
    birthday: date
    is_admin: bool


class LoginModel(BaseModel):
    login: str
    password: str


class PaginatedMetaDataModel(BaseModel):
    total: int
    page: int
    size: int


class PrivateCreateUserModel(BaseModel):
    first_name: str
    second_name: str
    other_name: str
    email: str
    phone: str
    city: int
    additional_info: str
    is_admin: bool
    password: str


class PrivateDetailUserResponseModel(BaseModel):
    id: int
    first_name: str
    second_name: str
    other_name: str
    email: str
    phone: str
    city: int
    additional_info: str
    is_admin: bool


class PrivateUpdateUserModel(BaseModel):
    id: int
    first_name: str
    second_name: str
    other_name: str
    email: str
    phone: str
    city: int
    additional_info: str
    is_admin: bool


class PrivateUsersListHintMetaModel(BaseModel):
    city: list[CitiesHintModel]


class PrivateUsersListMetaDataModel(BaseModel):
    pagination: PaginatedMetaDataModel
    hint: PrivateUsersListHintMetaModel


class UsersListElementModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


class PrivateUsersListResponseModel(BaseModel):
    data: UsersListElementModel
    meta: PrivateUsersListMetaDataModel


class UpdateUserModel(BaseModel):
    first_name: str
    last_name: str
    other_name: str
    email: str
    phone: str
    birthday: date


class UpdateUserResponseModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    other_name: str
    email: str
    phone: str
    birthday: date


class UsersListMetaDataModel(BaseModel):
    pagination: PaginatedMetaDataModel


class UsersListResponseModel(BaseModel):
    date: UsersListElementModel
    meta: UsersListMetaDataModel
