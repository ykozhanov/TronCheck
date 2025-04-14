from .domain_exceprions import BadRequestException


class HistoryPaginatorBadRequestException(BadRequestException):
    message = "Ошибка пагинации истории запросов информации Tron"
