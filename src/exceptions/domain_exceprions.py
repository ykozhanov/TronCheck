class DomainException(Exception):
    code = "domain_error"
    status_code = 500
    message = "Нарушение бизнес-правила"

    def __init__(self, message: str | None = None, **kwargs):
        self.message = message or self.message
        self.details = kwargs


class NotFoundException(DomainException):
    code = "not_found"
    status_code = 404
    message = "Ресурс не найден"


class ConflictException(DomainException):
    code = "conflict"
    status_code = 409
    message = "Конфликт с текущим состоянием ресурса"


class ValidationException(DomainException):
    code = "validation_failed"
    status_code = 422
    message = "Некорректные данные"

