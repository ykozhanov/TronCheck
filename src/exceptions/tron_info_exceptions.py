from .domain_exceprions import NotFoundException, BadRequestException


class AddressBadRequestException(BadRequestException):
    message = "Некорректный адрес"


class AddressNotFoundException(NotFoundException):
    message = "Адрес не найден"
