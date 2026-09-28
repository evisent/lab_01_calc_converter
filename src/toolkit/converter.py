from .errors import *

LENGTH = ['mm', 'cm', 'm', 'km']
WEIGHT = ['g', 'kg']
TEMPERATURE = ['c', 'f', 'k']


def get_unit_type(unit) -> str:
    """ Возвращает тип единицы измерения """

    if unit in LENGTH:
        return "length"
    elif unit in WEIGHT:
        return "weight"
    elif unit in TEMPERATURE:
        return "temperature"
    else:
        raise UnitError(unit)


def to_mm(value, from_) -> float:
    """ Переводит единицы длины в миллиметры """

    match from_:
        case "mm":
            return value
        case "cm":
            return value * 10
        case "m":
            return value * 1000
        case "km":
            return value * 1_000_000


def from_mm(value, to) -> float:
    """ Переводит миллиметры в целевую единицу измерения """

    match to:
        case "mm":
            return value
        case "cm":
            return value / 10
        case "m":
            return value / 1000
        case "km":
            return value / 1_000_000


def to_g(value, from_) -> float:
    """ Переводит единицы массы в граммы """

    match from_:
        case "g":
            return value
        case "kg":
            return value * 1000


def from_g(value, to) -> float:
    """ Переводит граммы в целевую единицу измерения """

    match to:
        case "g":
            return value
        case "kg":
            return value / 1000


def to_c(value, from_) -> float:
    """ Переводит единицы температуры в градусы цельсия """

    match from_:
        case "c":
            return value
        case "f":
            return (value - 32) / 1.8
        case "k":
            return value - 273.15


def from_c(value, to) -> float:
    """ Переводит градусы цельсия в целевую единицу измерения """

    if value < -273.15:
        raise TemperatureError()
    match to:
        case "c":
            return value
        case "f":
            return value * 1.8 + 32
        case "k":
            return value + 273.15


def convertation(value, from_unit, to_unit) -> float:
    """ Конвертирует единицы измерения
    :param value: Значение исходной единицы измерения
    :param from_unit: Единица измерения, из которой переводим
    :param to_unit: Единица измерения, в которую переводим
    """

    from_ = from_unit.strip().lower()
    to = to_unit.strip().lower()

    type_from = get_unit_type(from_)
    type_to = get_unit_type(to)

    if type_from != type_to:
        raise ConvertError(from_, to)
    match type_from:
        case "length":
            return from_mm(to_mm(value, from_), to)
        case "weight":
            return from_g(to_g(value, from_), to)
        case "temperature":
            return from_c(to_c(value, from_), to)