from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, HTTPException
from pydantic import ValidationError

from db import schemas


async def exception_handler(request: Request, exc: Exception):
    # Обработка всех исключений
    error_message = "Что-то пошло не так, мы уже исправляем эту ошибку"
    response_model = schemas.CodelessErrorResponseModel(message=error_message)
    return JSONResponse(status_code=500, content=response_model.dict())


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Обработка ошибок валидации запроса
    error_message = "Ошибка валидации данных"
    response_model = schemas.ErrorResponseModel(code=400, message=error_message)
    return JSONResponse(status_code=400, content=response_model.dict())


async def validation_error_handler(request: Request, exc: ValidationError):
    # Обработка ошибок валидации данных Pydantic
    error_message = "Ошибка валидации данных"
    response_model = schemas.ErrorResponseModel(code=400, message=error_message)
    return JSONResponse(status_code=400, content=response_model.dict())


async def http_exception_handler(request: Request, exc: HTTPException):
    # Обработка HTTP-исключений (например, 404 Not Found)
    error_message = exc.detail
    response_model = schemas.ErrorResponseModel(code=exc.status_code, message=error_message)
    return JSONResponse(status_code=exc.status_code, content=response_model.dict())
