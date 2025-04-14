class DomainException(Exception):
    code = "domain_error"
    status_code = 500
    message = "Нарушение бизнес-правила"

    def __init__(self, message: str | None = None, **kwargs):
        self.message = message or self.message
        self.details = kwargs


class BadRequestException(DomainException):
    code = "bad_request"
    status_code = 400
    message = "Некорректный запрос"


class NotFoundException(DomainException):
    code = "not_found"
    status_code = 404
    message = "Объект не найден"


class ValidationException(DomainException):
    code = "validation_failed"
    status_code = 422
    message = "Ошибка валидации"
