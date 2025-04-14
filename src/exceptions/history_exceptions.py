from .domain_exceprions import ValidationException


class HistoryPaginatorValidationException(ValidationException):
    code = 400
    message = "Ошибка пагинации истории запросов информации Tron"
