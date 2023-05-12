from fastapi import APIRouter
from fastapi.exceptions import RequestValidationError, HTTPException
from pydantic import ValidationError


router = APIRouter(
    prefix="/test",
    tags=["test"]
)


@router.get(
    "/test-other-errors",
    summary="Ошибка для пользователя",
    description="Генерируем исключение ValueError для тестирования обработки других ошибок"
)
def test_error():
    raise ValueError("Тестовая ошибка")


@router.get(
    "/test-validation-exception",
    summary="Ошибка обработки при валидации запроса",
    description="Генерируем исключение RequestValidationError для тестирования обработки ошибки валидации запроса"
)
def test_validation_exception():
    raise RequestValidationError("Ошибка валидации запроса")


@router.get(
    "/test-validation-error",
    summary="Ошибка обработки при валидации Pydantic",
    description="Генерируем исключение ValidationError для тестирования обработки ошибки валидации данных Pydantic"
)
def test_validation_error():
    raise ValidationError("Ошибка валидации данных")


@router.get(
    "/test-http-exception",
    summary="Ошибка http-исключения",
    description="Генерируем HTTP-исключение для тестирования обработки HTTP-исключений (например, 404 Not Found)"
)
def test_http_exception():
    raise HTTPException(status_code=404, detail="Ресурс не найден")
