from .domain_exceprions import NotFoundException


class TronAddressNotFoundException(NotFoundException):
    message = "Адрес не найден в блокчейн цепочке"